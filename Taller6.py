"""Taller 6.

Este archivo contiene un ejemplo funcional con funciones reutilizables,
validación básica y una entrada principal del programa.
"""

from __future__ import annotations


def sumar_numeros(numeros: list[int]) -> int:
    """Devuelve la suma de una lista de números enteros."""
    return sum(numeros)


def promedio(numeros: list[int]) -> float:
    """Calcula el promedio de una lista de números enteros."""
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    return sum(numeros) / len(numeros)


def main() -> None:
    """Función principal del programa."""
    datos = [10, 20, 30, 40, 50]

    print("Datos ingresados:", datos)
    print("Suma:", sumar_numeros(datos))
    print("Promedio:", promedio(datos))


if __name__ == "__main__":
    main()
