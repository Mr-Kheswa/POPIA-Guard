import sqlite3
import re
from flask import Flask, render_template, request, redirect, flash, url_for, session

app = Flask(__name__)
app.secret_key = 'sa_final_year_capstone_secure_clean_token_v2'
DB_FILE = 'popiaguard_clean.db'

def init_db():
    """Information Systems 3: Sets up database architecture and tracking ledgers."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        
        # Core entity table storing users with a dynamic role attribute
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                email_address TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT NOT NULL, -- 'Consumer' or 'Compliance_Officer'
                sa_id_number TEXT UNIQUE, -- Nullable if Auditor signs up without SA ID
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Compliance tracking table logging explicit user legal consent milestones
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Consent_Logs (
                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                marketing_opt_in INTEGER DEFAULT 0,
                third_party_share INTEGER DEFAULT 0,
                action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES Users(user_id)
            )
        ''')
        conn.commit()

def validate_sa_id(id_str):
    """Business Analysis 3 Core Rule: Validates standard 13-digit numerical configuration."""
    return bool(re.match(r'^[0-9]{13}$', id_str))

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Web Development 3: Handles consumer intake and dynamic Admin registration."""
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role') # Dynamic Role selector from HTML
        
        sa_id = request.form.get('sa_id')
        marketing = 1 if request.form.get('marketing') else 0
        third_party = 1 if request.form.get('third_party') else 0
        
        # If registering as a Consumer, validate the SA ID
        if role == 'Consumer':
            if not sa_id or not validate_sa_id(sa_id):
                flash('Error: Consumers must provide a valid 13-digit South African ID number.', 'danger')
                return render_template('register.html')
        else:
            # Admins do not require SA ID for profile sign up in this system scope
            sa_id = None

        try:
            with sqlite3.connect(DB_FILE) as conn:
                cursor = conn.cursor()
                
                # 1. Archive User Profile with chosen system authority role
                cursor.execute(
                    "INSERT INTO Users (full_name, email_address, password, role, sa_id_number) VALUES (?, ?, ?, ?, ?)",
                    (full_name, email, password, role, sa_id)
                )
                user_id = cursor.lastrowid
                
                # 2. Wire tracking logs only for consumers electing privacy data models
                if role == 'Consumer':
                    cursor.execute(
                        "INSERT INTO Consent_Logs (user_id, marketing_opt_in, third_party_share) VALUES (?, ?, ?)",
                        (user_id, marketing, third_party)
                    )
                conn.commit()
                
                flash(f'Success: Registered successfully as a {role.replace("_", " ")}! You can now log in.', 'success')
                return redirect(url_for('login'))
                
        except sqlite3.IntegrityError:
            flash('Error: This Email address or SA ID is already assigned to an active profile.', 'danger')
            
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Web Development 3: Queries database records to confirm and assign system sessions."""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        with sqlite3.connect(DB_FILE) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Users WHERE email_address = ? AND password = ?", (email, password))
            user = cursor.fetchone()
            
            if user:
                session['logged_in'] = True
                session['user_id'] = user['user_id']
                session['user_role'] = user['role']
                session['user_name'] = user['full_name']
                
                # Dynamic role-based structural routing logic block
                if user['role'] == 'Compliance_Officer':
                    return redirect(url_for('dashboard'))
                else:
                    # Route consumers directly to their personal privacy portal profile
                    return redirect(url_for('consumer_profile'))
            else:
                flash('Access Denied: Invalid combination credentials checked.', 'danger')
                
    return render_template('login.html')

@app.route('/consumer-profile')
def consumer_profile():
    """Web Development 3: Isolated profile interface rendering consumer privacy data maps."""
    # Safety Check: Block unauthenticated users or corporate staff from hitting this view
    if not session.get('logged_in') or session.get('user_role') != 'Consumer':
        flash('Notice: You must sign in to view your data file footprint.', 'info')
        return redirect(url_for('login'))
        
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # SQL query tracking the unique active consumer and their associated consent permissions
        cursor.execute('''
            SELECT Users.full_name, Users.email_address, Users.sa_id_number, Users.created_at,
                   Consent_Logs.marketing_opt_in, Consent_Logs.third_party_share, Consent_Logs.action_timestamp
            FROM Users
            LEFT JOIN Consent_Logs ON Users.user_id = Consent_Logs.user_id
            WHERE Users.user_id = ?
        ''', (session['user_id'],))
        profile_data = cursor.fetchone()
        
    return render_template('consumer_home.html', profile=profile_data)

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

@app.route('/compliance-dashboard')
def dashboard():
    """Web Development 3: Role-Based Access Control gate tracking compliance archives."""
    if not session.get('logged_in') or session.get('user_role') != 'Compliance_Officer':
        flash('Notice: You must authenticate as a Compliance Officer before entering this space.', 'info')
        return redirect(url_for('login'))
        
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Advanced SQL joining operation pulling user profiles together with explicit consent ledger paths
        cursor.execute('''
            SELECT Users.full_name, Users.sa_id_number, Users.email_address, 
                   Consent_Logs.marketing_opt_in, Consent_Logs.third_party_share, Consent_Logs.action_timestamp
            FROM Users
            JOIN Consent_Logs ON Users.user_id = Consent_Logs.user_id
            ORDER BY Consent_Logs.action_timestamp DESC
        ''')
        records = cursor.fetchall()
    return render_template('dashboard.html', records=records)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)