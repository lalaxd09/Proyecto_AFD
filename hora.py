import re

#patron= re.compile("\d{2}[:]\d{2}")
def hora_datos(hora):
    horas = re.compile("^\d{1,2}")
    if (re.search(horas, hora)):
        validar = horas.findall(hora)
        nueva_cadena = re.sub(horas, "", hora)
        print(validar)
        print(nueva_cadena)

    transicion_p = re.compile("^[:]")
    if (re.search(transicion_p, nueva_cadena)):
        validar_t = transicion_p.findall(nueva_cadena)
        nueva_cadena_t = re.sub(transicion_p, "", nueva_cadena)
        print(validar_t)
        print(nueva_cadena_t)

    minutos=re.compile("^\d{2}")
    if (re.search(minutos, nueva_cadena_t)):
        validar_m = minutos.findall(nueva_cadena_t)
        nueva_cadena_m = re.sub(minutos, "", nueva_cadena_t)
        print(validar_m)
        print(nueva_cadena_m)
    vacio=['']
    transicion=[]
    transicion.extend(vacio)
    transicion.extend(validar)
    transicion.extend(validar_t)
    transicion.extend(validar_m)



    return transicion
