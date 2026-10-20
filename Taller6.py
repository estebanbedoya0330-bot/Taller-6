
def buscar_comentarios(comentarios):
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
        return

    palabra = input("Palabra a buscar: ").strip().lower()
    if palabra == "":
        print("Debe escribir una palabra.")
        return

    encontrados = 0
    for i in range(len(comentarios)):
        if palabra in comentarios[i].lower():
            print("Comentario", i + 1, ":", comentarios[i])
            encontrados += 1

    if encontrados == 0:
        print("Búsqueda sin coincidencias para '" + palabra + "'.")
    else:
        print("Búsqueda exitosa:", encontrados, "comentario(s) encontrado(s).")
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
        print("La palabra '" + palabra + "' no aparece en el comentario.")
    else:
        print("La palabra '" + palabra + "' aparece", veces, "vez/veces.")def resumen_comentario(comentarios):
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

    resumen = (caracteres, len(palabras), apariciones)  # tupla inmutable

    print("\n--- RESUMEN ---")
    print("Caracteres:", resumen[0])
    print("Palabras:", resumen[1])
    print("Apariciones de '" + palabra + "':", resumen[2])
    return resumen
