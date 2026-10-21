import os
import sqlite3
import hashlib
import subprocess

# Hardcoded credentials
DB_PASSWORD = "admin123"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
API_KEY = "ghp_16C7e42F292c6912E7710c838347Ae298V4"

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    return cursor.fetchone()

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def run_command(user_input):
    os.system(f"echo {user_input}")

def get_file(path):
    full_path = "/var/data/" + path
    return open(full_path).read()

def fetch_url(url):
    import requests
    return requests.get(url).text
