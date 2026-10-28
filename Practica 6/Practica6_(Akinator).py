import json
import os

ARCHIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "akinator.json")


def cargar():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, encoding="utf-8") as f:
            return json.load(f)
    return {
        "pregunta": "¿Es una persona real?",
        "si": {"respuesta": "Albert Einstein"},
        "no": {"respuesta": "Harry Potter"},
    }


def guardar(arbol):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(arbol, f, ensure_ascii=False, indent=2)


def si(pregunta):
    while True:
        r = input(pregunta + " (s/n): ").strip().lower()
        if r in ("s", "si", "sí"):
            return True
        if r in ("n", "no"):
            return False


def jugar(nodo):
    while "pregunta" in nodo:
        nodo = nodo["si"] if si(nodo["pregunta"]) else nodo["no"]

    if si(f"¿Es {nodo['respuesta']}?"):
        print("¡Adiviné!")
        return

    nuevo = input("Me rindo. ¿Quién era? ").strip()
    pregunta = input(f"Pregunta que distinga a {nuevo} de {nodo['respuesta']}: ").strip()
    resp_nuevo = si(f"Para {nuevo}, ¿la respuesta es sí?")

    viejo = {"respuesta": nodo["respuesta"]}
    hoja = {"respuesta": nuevo}
    nodo.clear()
    nodo["pregunta"] = pregunta
    nodo["si"] = hoja if resp_nuevo else viejo
    nodo["no"] = viejo if resp_nuevo else hoja
    print("¡Gracias, aprendí algo nuevo!")


def main():
    arbol = cargar()
    print("Piensa en un personaje (real o ficticio) o en un videojuego")
    print("y yo intentaré adivinarlo.\n")
    while True:
        jugar(arbol)
        guardar(arbol)
        if not si("\n¿Jugamos otra vez?"):
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n¡Adiós!")
