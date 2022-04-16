import re

#patron= re.compile("\d{2}[:]\d{2}")
def hora_datos(hora):
    horas = re.compile("^\d{1,2}")
    if (re.search(horas, hora)):
        validar = horas.findall(hora)
        nueva_cadena = re.sub(horas, "", hora)
        print(validar)
        print(nueva_cadena)

    transicion = re.compile("^[:]")
    if (re.search(transicion, nueva_cadena)):
        validar_t = transicion.findall(nueva_cadena)
        nueva_cadena_t = re.sub(transicion, "", nueva_cadena)
        print(validar_t)
        print(nueva_cadena_t)

    minutos=re.compile("^\d{2}")
    if (re.search(minutos, nueva_cadena_t)):
        validar_m = minutos.findall(nueva_cadena_t)
        nueva_cadena_m = re.sub(minutos, "", nueva_cadena_t)
        print(validar_m)
        print(nueva_cadena_m)

    estados=[]
    estados.extend(validar)
    estados.extend(validar_m)

    transicion=[':']


    return estados,transicion
