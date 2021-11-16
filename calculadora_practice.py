print('Bienvenido a nuestra calculadora, por favor, seleccione una de las siguientes opciones: ')
seguir = 0
x = 0
while seguir == 0:
    if x > 0:
        print('Quieres seguir realizando operaciones?')
        respuesta = input('S = Si o N = No: ')
        respuesta = respuesta.upper()
        while respuesta != 'S' and respuesta != 'N':
            print('No ha seleccionado una respuesta valida, por favor intente nuevamente')
            print('Quieres seguir realizando operaciones?')
            respuesta = input('S = Si o N = No: ')
            respuesta = respuesta.upper()
        if respuesta == 'N':
            exit()
    x += 1
    operacion = int(input('1- Suma    2- Resta    3-Multiplicación    4- División   5- Cancelar: '))
    while operacion != 1 and operacion != 2 and operacion != 3 and operacion != 4:
        if operacion == 5:
            seguir = 1
            exit()
        print('No has seleccionado ninguna de las opciones disponibles, intenta nuevamente.')
        operacion = int(input('1- Suma    2- Resta    3-Multiplicación    4- División   5- Cancelar: '))

    a = float(input('Escribe el primer numero: '))
    b = float(input('Escribe el segundo numero: '))
    def suma():
        resultado = a + b
        if resultado % 2 == 0:
            print('El resultado de la suma es: ', int(resultado))
        else:
            print('El resultado de la suma es: ', resultado)
    def resta():
        resultado = a - b
        if resultado % 2 == 0:
            print('El resultado de la resta es: ', int(resultado))
        else:
            print('El resultado de la resta es: ', resultado)
    def multi():
        resultado = a * b
        if resultado % 2 == 0:
            print('El resultado de la multiplicación es: ', int(resultado))
        else:
            print('El resultado de la multiplicación es: ', resultado)
    def division():
        resultado = a / b
        if resultado % 2 == 0:
            print('El resultado de la división es: ', int(resultado))
        else:
            print('El resultado de la división es: ', resultado)

    if operacion == 1:
        suma()
    elif operacion == 2:
        resta()
    elif operacion == 3:
        multi()
    else:
        division()
