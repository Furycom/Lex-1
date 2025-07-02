import os
import hashlib
from datetime import datetime
from pathlib import Path
import subprocess

FILENAME = "data/yann.md"
CONTENT = f"# Fichier de test Yann\n\nCe fichier a été généré automatiquement par Lex-1.\nDate : {datetime.utcnow().isoformat()}Z\n"

def sha256(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def file_needs_update(path, content):
    if not os.path.exists(path):
        return True
    with open(path, "r", encoding="utf-8") as f:
        existing_content = f.read()
    return sha256(existing_content) != sha256(content)

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def git_commit_and_push(path):
    subprocess.run(["git", "config", "--global", "user.name", "lex1-actions"], check=True)
    subprocess.run(["git", "config", "--global", "user.email", "lex1-actions@furycom"], check=True)
    subprocess.run(["git", "add", path], check=True)
    subprocess.run(["git", "commit", "-m", "Création automatique de yann.md par Lex-1"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

if file_needs_update(FILENAME, CONTENT):
    write_file(FILENAME, CONTENT)
    git_commit_and_push(FILENAME)
else:
    print("Aucun changement détecté. Aucune action requise.")
