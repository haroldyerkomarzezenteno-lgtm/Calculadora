from operaciones import (
    calcular_potencia,
    calcular_modulo,
    calcular_raiz_cuadrada,
    calcular_porcentaje,
    calcular_valor_absoluto,
    calcular_factorial,
    calcular_promedio,
    calcular_redondeo
)

def mostrar_menu():
    print("\n==============================")
    print("    CALCULADORA CIENTÍFICA    ")
    print("==============================")
    print("1. Potencia")
    print("2. Módulo")
    print("3. Raíz cuadrada")
    print("4. Porcentaje")
    print("5. Valor absoluto")
    print("6. Factorial")
    print("7. Promedio")
    print("8. Redondeo")
    print("9. Salir")

def ejecutar_calculadora():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-9): ")

        if opcion == "9":
            print("¡Gracias por utilizar la calculadora! Saliendo...")
            break

        try:
            if opcion == "1":
                base = float(input("Ingrese la base: "))
                exponente = float(input("Ingrese el exponente: "))
                resultado = calcular_potencia(base, exponente)
                print(f"Resultado: {resultado}")

            elif opcion == "2":
                a = float(input("Ingrese el dividendo: "))
                b = float(input("Ingrese el divisor: "))
                resultado = calcular_modulo(a, b)
                print(f"Resultado: {resultado}")

            elif opcion == "3":
                n = float(input("Ingrese el número: "))
                resultado = calcular_raiz_cuadrada(n)
                print(f"Resultado: {resultado}")

            elif opcion == "4":
                cantidad = float(input("Ingrese la cantidad total: "))
                porcentaje = float(input("Ingrese el porcentaje a calcular: "))
                resultado = calcular_porcentaje(cantidad, porcentaje)
                print(f"Resultado: {resultado}")

            elif opcion == "5":
                n = float(input("Ingrese el número: "))
                resultado = calcular_valor_absoluto(n)
                print(f"Resultado: {resultado}")

            elif opcion == "6":
                n = int(input("Ingrese un número entero no negativo: "))
                resultado = calcular_factorial(n)
                print(f"Resultado: {resultado}")

            elif opcion == "7":
                entrada = input("Ingrese los números separados por espacio: ")
                lista_numeros = [float(x) for x in entrada.split()]
                resultado = calcular_promedio(lista_numeros)
                print(f"Resultado: {resultado}")

            elif opcion == "8":
                valor = float(input("Ingrese el número a redondear: "))
                decimales = int(input("Ingrese la cantidad de decimales: "))
                resultado = calcular_redondeo(valor, decimales)
                print(f"Resultado: {resultado}")

            else:
                print("Opción inválida. Por favor, elija un número entre 1 y 9.")

        except ValueError as e:
            print(f"Error de entrada o cálculo: {e}")
        except ZeroDivisionError:
            print("Error: División entre cero no permitida.")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    ejecutar_calculadora()