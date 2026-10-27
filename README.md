# POPIA-Guard: Multi-Tenant Identity Verification & Privacy Engine
A full-stack, enterprise microservice designed to handle compliant user data intake and secure administrative ledger tracking under South African regulatory guidelines. This application acts as an integrated capstone project executing competencies from my final year modules: **Business Analysis 3**, **Information Systems 3**, and **Web Development 3**. For educational experience and learning purposes.

---

## Module Core Architecture
### 1. Business Analysis 3 (Governance & Requirements)
* **Regulatory Compliance Framework:** Designed workflows that strictly observe the Protection of Personal Information Act (POPIA), Act 4 of 2013, specifically targeting Section 24 (The Right to Correction and Deletion).
* **Multi-Tenant Personas:** Formulated distinct, insulated system paths for **Consumers (Data Subjects)** to view their privacy profiles and **Compliance Officers (Auditors)** to manage the corporate data ecosystem.
* **Risk Register:** Drafted internal checks to prevent legal penalties, unauthorized data extraction, or improper marketing ingestion.

### 2. Information Systems 3 (Relational Database Design)
* **Schema Integrity:** Architected a normalized relational schema built natively over an isolated SQLite processing pipeline.
* **Identity Validation Logic:** Enforced backend constraints using custom regex validation routines to programmatically check the exact 13-digit numerical configuration of South African identity strings before writing records.
* **Immutable Data Trails:** Engineered a decoupled `Consent_Logs` data index ledger linking to the core `Users` master table to track opt-in configurations securely without compromising core historical analytics required by SARS.

### 3. Web Development 3 (Full-Stack Software Development)
* **Backend Ingestion Engine:** Programmed robust request routing mechanisms, role-based boundary checkpoints, and data type-casting using **Python** and the **Flask** environment ecosystem.
* **Advanced Client-Side UI:** Deployed a responsive, mobile-first frontend framework featuring custom HTML5 semantics and structured CSS3 parameters.
* **Dynamic Interface Layouts:** Utilized local **JavaScript** listeners to manipulate form elements dynamically, adjusting data constraints automatically when a user switches roles from Consumer to Compliance Auditor.

---

## Design & Aesthetic Choices
* **Palette Strategy:** Formulated using custom light CSS variables to create an inclusive, highly modern environment accessible across all devices and neutral for all user demographics.
* **Text Alignment:** Configured with clean, legible serif typography heights and symmetrical spacing grid pads to maximize scanning speed for high-volume corporate auditing workflows.

---

## Step-by-Step Installation & Running Guide

### 1. Prerequisite Installations
Ensure you have Python installed on your local computer. Open your built-in terminal inside **VS Code** and run:
```bash
pip install flask
```
*Note: This architecture utilizes a native embedded database, eliminating the need to install external SQL database drivers or extensions inside VS Code.*

### 2. Project Directory Setup
Ensure your local project directory structure matches the following exactly:
```text
popiaguard_clean/
│
├── app.py                  <-- Core Python Engine
└── templates/
    ├── register.html       <-- Portal Intake Form
    ├── login.html          <-- Audit Room Authentication
    ├── dashboard.html      <-- Corporate Records Table
    └── consumer_home.html  <-- Personal Privacy Vault
```

### 3. Executing the Local Server Instance
From your terminal room workspace folder directory, initialize the background server runtime execution script by running:
```bash
python app.py
```

### 4. Interactive Simulation Matrix
Once running locally, pull up your web browser to check the user interaction paths:
1. **Consumer Portal Onboarding:** Navigate to `http://127.0.0`. Fill in the parameters choosing the **Consumer** role option, and select your privacy toggle configurations. Click submit.
2. **Account Access Verification:** You will slide directly into the Account Sign-In gateway room. Key in the consumer credentials you just generated to view your isolated personal privacy profile vault map.
3. **Administrative Access Audit:** Log out, return to the register node, select **Compliance Officer**, and complete a new corporate profile creation script. Log into that account to view the entire master ledger table sheet containing all logged data records.

---

## Security & RBAC Boundaries
This platform operates with strict **Role-Based Access Control (RBAC)** filters. If an unauthenticated user or general consumer configuration attempts to skip standard layout interfaces by manually altering target URLs to access corporate pipelines (such as `/compliance-dashboard`), backend server tracking cookies instantly block the request and securely route traffic back to the authentication portal login gate.
