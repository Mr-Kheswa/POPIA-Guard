# POPIA-Guard: Multi-Tenant Identity Verification & Privacy Engine
A full-stack, enterprise microservice designed to handle compliant user data intake and secure administrative ledger tracking under South African regulatory guidelines. This application acts as an integrated capstone project executing competencies from my final year modules: **Business Analysis 3**, **Information Systems 3**, and **Web Development 3**. For educational experience and learning purposes.

---

## Module Core Architecture
### 1. Business Analysis 3 (Governance & Requirements)
### 2. Information Systems 3 (Relational Database Design)
### 3. Web Development 3 (Full-Stack Software Development)

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
