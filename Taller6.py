import re


def buscar_comentarios(comentarios):
    """Busca una palabra dentro de todos los comentarios."""
    if not comentarios:
        print("No hay comentarios registrados.")
        return

    palabra = input("Palabra a buscar: ").strip().lower()
    if palabra == "":
        print("Debe escribir una palabra.")
        return

    encontrados = 0
    for i, comentario in enumerate(comentarios, start=1):
        if palabra in comentario.lower():
            print(f"Comentario {i}: {comentario}")
            encontrados += 1

    if encontrados == 0:
        print(f"Búsqueda sin coincidencias para '{palabra}'.")
    else:
        print(f"Búsqueda exitosa: {encontrados} comentario(s) encontrado(s).")


def limpiar_palabras(texto):
    """Devuelve una lista de palabras limpias en minúsculas."""
    return re.findall(r"[A-Za-zÁÉÍÓÚáéíóúÜüÑñ]+", texto.lower())


def elegir_comentario(comentarios):
    """Muestra los comentarios y devuelve el texto seleccionado."""
    if not comentarios:
        print("No hay comentarios registrados.")
        return None

    for i, comentario in enumerate(comentarios, start=1):
        print(f"{i}. {comentario}")

    opcion = input("Selecciona el número del comentario: ").strip()
    if opcion == "":
        print("Debe ingresar un número.")
        return None

    try:
        indice = int(opcion) - 1
    except ValueError:
        print("Debe ingresar un número válido.")
        return None

    if 0 <= indice < len(comentarios):
        return comentarios[indice]

    print("Número fuera de rango.")
    return None


def contar_palabra(comentarios):
    """Cuenta cuántas veces aparece una palabra en un comentario elegido."""
    if not comentarios:
        print("No hay comentarios registrados.")
        return

    texto = elegir_comentario(comentarios)
    if texto is None:
        return

    palabra = input("Palabra a contar: ").strip().lower()
    if palabra == "":
        print("Debe escribir una palabra.")
        return

    palabras = limpiar_palabras(texto)
    veces = palabras.count(palabra)

    if veces == 0:
        print(f"La palabra '{palabra}' no aparece en el comentario.")
    else:
        print(f"La palabra '{palabra}' aparece {veces} vez/veces.")


def resumen_comentario(comentarios):
    """Devuelve un resumen de caracteres, palabras y apariciones."""
    if not comentarios:
        print("No hay comentarios registrados.")
        return None

    texto = elegir_comentario(comentarios)
    if texto is None:
        return None

    palabra = input("Palabra a buscar en el comentario: ").strip().lower()

    caracteres = len(texto)
    palabras = limpiar_palabras(texto)
    apariciones = palabras.count(palabra) if palabra != "" else 0
    resumen = (caracteres, len(palabras), apariciones)

    print("\n--- RESUMEN ---")
    print(f"Caracteres: {resumen[0]}")
    print(f"Palabras: {resumen[1]}")
    print(f"Apariciones de '{palabra}': {resumen[2]}")
    return resumen


def menu():
    """Menú de prueba para ejecutar las funciones del taller."""
    comentarios = [
        "Me gusta mucho este curso de Python.",
        "El proyecto es interesante y muy útil.",
        "Python es un lenguaje poderoso y sencillo.",
        "Me encanta programar en Python todos los días.",
        "El curso fue interesante, pero necesito practicar más."
    ]

    while True:
        print("\n=== MENÚ ===")
        print("1. Buscar comentarios")
        print("2. Contar palabra en un comentario")
        print("3. Resumen de un comentario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            buscar_comentarios(comentarios)
        elif opcion == "2":
            contar_palabra(comentarios)
        elif opcion == "3":
            resumen_comentario(comentarios)
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
