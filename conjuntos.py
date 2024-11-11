def agregar_conjunto():
    conjunto = set()
    elementos = input("Introduce los elementos separados por comas: ")
    for elemento in elementos.split(","):
        conjunto.add(elemento.strip())
    return conjunto

def imprimir_conjunto(conjunto, nombre):
    print(f"{nombre}: {conjunto}")

def main():
    conjunto1 = set()
    conjunto2 = set()
    
    while True:
        print("\n--- Menú ---")
        print("1. Agregar conjunto 1")
        print("2. Agregar conjunto 2")
        print("3. Calcular la unión de los conjuntos e imprimir el resultado")
        print("4. Calcular la intersección de los conjuntos e imprimir el resultado")
        print("5. Imprimir los conjuntos")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            conjunto1 = agregar_conjunto()
            print("Conjunto 1 agregado.")
        elif opcion == "2":
            conjunto2 = agregar_conjunto()
            print("Conjunto 2 agregado.")
        elif opcion == "3":
            union = conjunto1.union(conjunto2)
            print("Unión de los conjuntos:", union)
        elif opcion == "4":
            interseccion = conjunto1.intersection(conjunto2)
            print("Intersección de los conjuntos:", interseccion)
        elif opcion == "5":
            imprimir_conjunto(conjunto1, "Conjunto 1")
            imprimir_conjunto(conjunto2, "Conjunto 2")
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()
