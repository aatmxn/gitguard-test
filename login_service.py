import os
import sqlite3
import hashlib
import subprocess

# Hardcoded secrets - NEVER do this in production
SECRET_API_KEY = "ghp_16C7e42F292c6912E7710c838347Ae298V4"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASSWORD = "admin123"

def authenticate_user(username, password):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # SQL Injection: user input directly in query
    query = "SELECT * FROM users WHERE user='" + username + "' AND pass='" + password + "'"
    cursor.execute(query)
    return cursor.fetchone()

def hash_secret(value):
    # MD5 is cryptographically broken for passwords
    return hashlib.md5(value.encode()).hexdigest()

def execute_report(report_name):
    # Command injection: unsanitized shell execution
    os.system("generate_report.sh " + report_name)

def read_config(filename):
    # Path traversal: attacker can read /etc/passwd with ../../etc/passwd
    base = "/app/configs/"
    return open(base + filename).read()

def fetch_resource(url):
    # SSRF: unvalidated outbound request
    import urllib.request
    return urllib.request.urlopen(url).read()

def run_user_script(code):
    # Remote code execution via eval
    return eval(code)
