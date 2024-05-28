# Suma de dos números

def sumar_numeros(a, b):
    return a + b

def main():
    try:
        # Solicita al usuario que ingrese dos números
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
        
        # Calcula la suma de los dos números
        resultado = sumar_numeros(numero1, numero2)
        
        # Muestra el resultado
        print(f"La suma de {numero1} y {numero2} es {resultado}")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()
