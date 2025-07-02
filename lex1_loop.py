import os

def main():
    print("Début du test de Lex-1 dans GitHub Actions.")
    
    try:
        with open("data/yann.md", "w") as f:
            f.write("Fichier généré automatiquement par Lex-1.\n")

        print("Fichier 'yann.md' créé localement dans le dépôt.")
        
        print("Le fichier est prêt à être committé et poussé par le workflow.")

    except Exception as e:
        print(f"Erreur détectée : {e}")

if __name__ == "__main__":
    main()
