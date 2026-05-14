
intento = 3
while intento > 0:
    contraseña = int(input("Escribe tu contraseña: "))
    if contraseña == 123:
        print("La contraseña es correcta")
        break
    else:
        intento -= 1
        print("la contraseña es incorrecta intenta de nuevo", intento)
if intento == 0: 
    print("cuenta bloqueada")