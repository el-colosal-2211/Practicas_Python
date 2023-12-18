num1 = int(input("Digíta el primer valor: "))
num2 = int(input("Digíta el segundo valor: "))

select = 0

while select != 6:
    print("""
    Indique que tipo de operación matemática va a realizar:

    1. Suma
    2. Resta
    3. Multiplicación 
    4. División
    5. Cambiar Valores
    6. Salir
    """)

    select = int(input())

    if select == 1:
        print(" ")
        print("El resultado de: ", num1, "+", num2, "=", num1+num2)

    if select == 2:
        print(" ")
        print("El resultado de: ", num1, "-", num2, "=", num1-num2)

    if select == 3:
        print(" ")
        print("El resultado de: ", num1, "*", num2, "=", num1*num2) 

    if select == 4:
        print(" ")
        print("El resultado de: ", num1, "/", num2, "=", num1/num2)

    if select == 5:
        num1 = int(input("Digíta el primer valor: "))
        num2 = int(input("Digíta el segundo valor: "))

    if select == 6:
        print("*Gracias por usar nuestra calculadora*")