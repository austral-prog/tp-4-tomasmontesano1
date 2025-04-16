def leap_year():
    a=int(input('Ingrese un año: '))
    b = a%4==0 and a%100!=0
    if (b) or (a%100==0 and a%400==0):
        print(f'El año {a} es bisiesto')
    else:
        print(f'El año {a} no es bisiesto')
