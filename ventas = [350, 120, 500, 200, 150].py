ventas = [350, 120, 500, 200, 150]
swappped = True 


while swappped:
    swappped = False
    for i in range(len (ventas) -1):
        if ventas[i] > ventas[i +1]:
            swappped = True
            ventas[i], ventas[i +1] = ventas[i +1], ventas[i]
    print("orden de la lsitas es: ", ventas)    

mayor = max(ventas)
menor = min(ventas)

print("El numero mayor de ventas es ", mayor)
print("El numero menor de ventas es: ", menor)    
total = 0

for i in range(len(ventas)):
    total += ventas[i]

print("Total de ventas:", total)

promedio = total
promedio = total / len(ventas)
print("El promedio de ventas es: ", promedio)    
