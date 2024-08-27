#usar parentesis al hacer operaciones matematicas nada eso todo es re raris
print("Bienvenido. Esta es una calculadora de suma y resta (ya se re tonto pero es mi primer codigo). Estas operaciones se realizarán individualmente, por lo que depende del valor que ingrese. Si desea sumar, ingrese (1), en cambio, si desea restar, ingrese (2)")
while True :
    while True :
        try :
            op = int(input("opción = "))
            break
        except ValueError :
            print("no es un int")
    if op == 1 :
        print("\nSe realizará una SUMA\nIngrese dos números a su preferencia")
        num1 = int(input("número 1 = "))
        num2 = int(input("número 2 = "))
        print(f"{num1} + {num2} = {num1+num2}")
        break
    elif op == 2 :
        print("\nSe realizará una RESTA\nIngrese dos números a su preferencia")
        num1 = int(input("número 1 = "))
        num2 = int(input("número 2 = "))
        print(f"{num1} - {num2} = {num1-num2}") #otra forma de printear cosas re cool esto bro
        break
    else :
        print("opción no adecuada")






