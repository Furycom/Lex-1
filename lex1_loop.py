import os

def main():
    print("Début du test de Lex-1 dans GitHub Actions.")
    
    try:
        with open("data/yann.md", "w") as f:
            f.write("Fichier généré automatiquement par Lex-1.\n")

        print("Fichier 'yann.md' créé localement dans le dépôt.")
        
        os.system("git config user.email 'lex1@furycom.org'")
        os.system("git config user.name 'Lex-1'")
        os.system("git add data/yann.md")
        os.system("git commit -m 'Test: création automatique du fichier yann.md'")
        
        print("Les commandes git add et commit ont été exécutées.")
        print("ATTENTION : git push désactivé temporairement pour éviter le blocage.")
        
        # subprocess.run(["git", "push", "origin", "main"], check=True)

    except Exception as e:
        print(f"Erreur détectée : {e}")

if __name__ == "__main__":
    main()
