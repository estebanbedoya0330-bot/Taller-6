import re

# 1
def buscar_comentarios(comentarios):
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
        return

    palabra = input("Palabra a buscar: ").strip().lower()
    if palabra == "":
        print("Debe escribir una palabra.")
        return

    encontrados = 0
    for i, comentario in enumerate(comentarios, start=1):
        if palabra in comentario.lower():
            print("Comentario", i, ":", comentario)
            encontrados += 1

    if encontrados == 0:
        print(f"Búsqueda sin coincidencias para '{palabra}'.")
    else:
        print(f"Búsqueda exitosa: {encontrados} comentario(s) encontrado(s).")


def limpiar_palabras(texto):
    return re.findall(r"[A-Za-zÁÉÍÓÚáéíóúÜüÑñ]+", texto.lower())


def elegir_comentario(comentarios):
    if len(comentarios) == 0:
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


# 2
def contar_palabra(comentarios):
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
        return

    texto = elegir_comentario(comentarios)
    if texto is None:
        return

    palabra = input("Palabra a contar: ").strip().lower()
    if palabra == "":
        print("Debe escribir una palabra.")
        return

    veces = limpiar_palabras(texto).count(palabra)
    if veces == 0:
        print(f"La palabra '{palabra}' no aparece en el comentario.")
    else:
        print(f"La palabra '{palabra}' aparece {veces} vez/veces.")


# 3
def resumen_comentario(comentarios):
    if len(comentarios) == 0:
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
    print("Caracteres:", resumen[0])
    print("Palabras:", resumen[1])
    print(f"Apariciones de '{palabra}':", resumen[2])
    return resumen
