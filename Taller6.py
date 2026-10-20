#1
frase = input("Escriba una frase: ").strip()

print("Frase:", frase)
print("Minusculas:", frase.lower())
print("Mayusculas:", frase.upper())

cantidad_caracteres = len(frase)
palabras = frase.split()
cantidad_palabras = len(palabras)

print("Caracteres:", cantidad_caracteres)
print("Palabras:", cantidad_palabras)

letra = input("Que letra desea contar?: ").strip().lower()
cantidad_letra = frase.lower().count(letra)

print("\n--- PALABRAS ---")
for i in range(len(palabras)):
    print(i + 1, palabras[i])

resumen = (
    cantidad_caracteres,
    cantidad_palabras,
    cantidad_letra
)

print("\n--- RESUMEN ---")
print("Caracteres:", resumen[0])
print("Palabras:", resumen[1])
print("Apariciones de la letra:", resumen[2])

#2

comentarios = []


def registrar_comentario():
    texto = input("Escriba el comentario: ").strip()

    if texto != "":
        comentarios.append(texto)
        print("Comentario registrado correctamente.")
    else:
        print("El comentario no puede estar vacio.")


def mostrar_comentarios():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
    else:
        print("\n--- COMENTARIOS REGISTRADOS ---")

        for i in range(len(comentarios)):
            print(i + 1, ".", comentarios[i])


def buscar_comentarios():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
        return

    palabra = input("Escriba la palabra que desea buscar: ")
    palabra = palabra.strip().lower()
    encontrado = False

    for i in range(len(comentarios)):
        texto = comentarios[i].lower()

        if palabra in texto:
            print(i + 1, ".", comentarios[i])
            encontrado = True

    if encontrado == False:
        print("No se encontraron comentarios con esa palabra.")


def contar_palabras():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
        return

    print("\n--- CANTIDAD DE PALABRAS ---")

    for i in range(len(comentarios)):
        palabras = comentarios[i].split()
        print("Comentario", i + 1, ":", len(palabras), "palabras")


def seleccionar_comentario():
    if len(comentarios) == 0:
        print("No hay comentarios registrados.")
        return -1

    mostrar_comentarios()

    try:
        numero = int(input("Seleccione el numero del comentario: "))

        if numero >= 1 and numero <= len(comentarios):
            return numero - 1
        else:
            print("Numero de comentario no valido.")
            return -1

    except ValueError:
        print("Debe ingresar un numero entero.")
        return -1


def contar_apariciones():
    posicion = seleccionar_comentario()

    if posicion == -1:
        return

    palabra = input("Escriba la palabra que desea contar: ")
    palabra = palabra.strip().lower()

    texto = comentarios[posicion].lower()
    cantidad = texto.count(palabra)

    print("La palabra aparece", cantidad, "veces.")
    
#3

def mostrar_resumen():
    posicion = seleccionar_comentario()

    if posicion == -1:
        return

    texto = comentarios[posicion]
    palabras = texto.split()

    palabra = input("Escriba la palabra que desea contar: ")
    palabra = palabra.strip().lower()

    cantidad_caracteres = len(texto)
    cantidad_palabras = len(palabras)
    cantidad_apariciones = texto.lower().count(palabra)

    resumen = (
        cantidad_caracteres,
        cantidad_palabras,
        cantidad_apariciones
    )

    print("\n--- RESUMEN DEL COMENTARIO ---")
    print("Caracteres:", resumen[0])
    print("Palabras:", resumen[1])
    print("Apariciones de la palabra:", resumen[2])
    print("Tupla del resumen:", resumen)


def menu():
    while True:
        print("\n===== ANALIZADOR DE COMENTARIOS =====")
        print("1. Registrar un comentario")
        print("2. Mostrar todos los comentarios")
        print("3. Buscar comentarios por palabra")
        print("4. Mostrar cantidad de palabras")
        print("5. Contar apariciones de una palabra")
        print("6. Mostrar resumen de un comentario")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_comentario()
        elif opcion == "2":
            mostrar_comentarios()
        elif opcion == "3":
            buscar_comentarios()
        elif opcion == "4":
            contar_palabras()
        elif opcion == "5":
            contar_apariciones()
        elif opcion == "6":
            mostrar_resumen()
        elif opcion == "7":
            print("Gracias por utilizar el programa.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


menu()
