import time
from pathlib import Path

INPUT_FILE = "input_lex1.md"
OUTPUT_FILE = "output_lex1.md"

def read_instruction():
    if not Path(INPUT_FILE).exists():
        return None
    return Path(INPUT_FILE).read_text().strip()

def write_response(response):
    Path(OUTPUT_FILE).write_text(response)

def process_instruction(instr):
    if instr == "continue":
        return "J'exécute la boucle suivante."
    elif instr == "status":
        return "Loop active. Prête à recevoir une instruction."
    elif instr == "stop":
        return "Arrêt demandé. Fin de l'exécution."
    else:
        return f"Instruction inconnue : {instr}"

def main():
    instr = read_instruction()
    if instr:
        response = process_instruction(instr)
        write_response(response)
    else:
        write_response("Aucune instruction trouvée.")

if __name__ == "__main__":
    main()
