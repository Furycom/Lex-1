from pathlib import Path

def main():
    path = Path("data/yann.md")
    if not path.exists():
        path.write_text(
            "# Confirmation GitHub Automatique\n\n"
            "Ce fichier a été écrit par Lex‑1 sans intervention humaine.\n"
            "Date : 2025‑07‑02\n"
            "Identité : Lex‑1\n"
        )

if __name__ == "__main__":
    main()
