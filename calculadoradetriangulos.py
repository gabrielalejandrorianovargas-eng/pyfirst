
import math

while True:
    print("\n=== CALCULADORA DE TRIÁNGULOS ===")
    print("1. Ingresar 2 lados")
    print("2. Ingresar 1 lado y 1 ángulo")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("\n--- INGRESO DE LADOS ---")
        
        try:
         a = float(input("Ingresa el lado a: "))
         b = float(input("Ingresa el lado b: "))
        except:
         print("ingresa numeros validos")
         continue


        hipotenusa = math.sqrt(a**2 + b**2)
        print(f"Hipotenusa: {hipotenusa:.2f}")

        seno = a / hipotenusa
        coseno = b / hipotenusa

        if b != 0:
            tangente = a / b
        else:
            tangente = 0

        print(f"Seno: {seno:.2f}")
        print(f"Coseno: {coseno:.2f}")
        print(f"Tangente: {tangente:.2f}")

    elif opcion == "2":
        print("\n--- ÁNGULO + HIPOTENUSA ---")

        angulo = float(input("Ingresa el ángulo en grados: "))
        hipotenusa = float(input("Ingresa la hipotenusa: "))

        rad = math.radians(angulo)

        opuesto = hipotenusa * math.sin(rad)
        adyacente = hipotenusa * math.cos(rad)

        print(f"Cateto opuesto: {opuesto:.2f}")
        print(f"Cateto adyacente: {adyacente:.2f}")

        print(f"Seno: {math.sin(rad):.2f}")
        print(f"Coseno: {math.cos(rad):.2f}")
        print(f"Tangente: {math.tan(rad):.2f}")

    elif opcion == "3":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")