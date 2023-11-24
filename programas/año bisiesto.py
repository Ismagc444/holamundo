def calculo(year):
    prueba1 =year% 4
    prueba2 =year%100
    prueba3 =year%400

    if prueba1==0 and (prueba3==0 or prueba2!=0):
        return True
    else:
        return False
year=int(input("introduce un año"))
resultado=calculo(year)
