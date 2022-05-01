import re



# Establecemos los formatos admitidos de fechas (dd/mm/aaaa o aaaa/mm/dd)(
#patron = re.compile("\d{1,2}[/]\d{1,2}[/]\d{4}|\d{4}[/]\d{1,2}[/]\d{1,2}")
def fechas_datos(fechas):
    #fecha=input("Ingrese fecha :")

    dias=re.compile("^\d{1,2}")
    if (re.search(dias, fechas)):
        validar = dias.findall(fechas)
        nueva_cadena = re.sub(dias, "", fechas)
        print(validar)
        print(nueva_cadena)


    transicion=re.compile("^/")
    if (re.search(transicion, nueva_cadena)):
        validar_t = transicion.findall(nueva_cadena)
        nueva_cadena_t = re.sub(transicion, "", nueva_cadena)
        print(validar_t)
        print(nueva_cadena_t)

    meses=re.compile("^\d{1,2}")
    if (re.search(meses, nueva_cadena_t)):
        validar_m = meses.findall(nueva_cadena_t)
        nueva_cadena_m = re.sub(meses, "", nueva_cadena_t)
        print(validar_m)
        print(nueva_cadena_m)


    transicion_2=re.compile("^/")
    if (re.search(transicion_2, nueva_cadena_m)):
        validar_2 = transicion_2.findall(nueva_cadena_m)
        nueva_cadena_2 = re.sub(transicion_2, "", nueva_cadena_m)
        print(validar_2)
        print(nueva_cadena_2)

    años=re.compile("\d{4}")
    if (re.search(años, nueva_cadena_2)):
        validar_a= años.findall(nueva_cadena_2)
        nueva_cadena_a = re.sub(años, "", nueva_cadena_2)
        print(validar_a)
        print(nueva_cadena_a)

    transiciones=[]
    diagonal = ['/']
    diagonal_2=['/']
    vacio=['']
    transiciones.extend(vacio)
    transiciones.extend(validar)
    transiciones.extend(validar_m)
    transiciones.extend(validar_a)
    transiciones.extend(diagonal)
    transiciones.extend(diagonal_2)

    return transiciones




