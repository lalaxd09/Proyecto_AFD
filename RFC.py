import re
#("^([A-ZÑ\x26]{3,4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1]))([A-Z\d]{3})?$")
def RFCD(rfc):


    primeras_letras = re.compile("^([A-ZÑ\x26]{3,4})")
    if (re.search(primeras_letras, rfc)):
        validar = primeras_letras.findall(rfc)
        nueva_cadena = re.sub(primeras_letras, "", rfc)
        #print(validar)
        #print(nueva_cadena)

    creacion_fecha=re.compile("\d{6}")
    if (re.search(creacion_fecha, nueva_cadena)):
        validar_f = creacion_fecha.findall(nueva_cadena)
        nueva_cadena_f = re.sub(creacion_fecha, "", nueva_cadena)
        #print('creacion')
        #print(validar_f)
        #print(nueva_cadena_f)

    homoclave=re.compile("[A-Z\d]{3}?$")
    if (re.search(homoclave, nueva_cadena_f)):
        validar_h = homoclave.findall(nueva_cadena_f)
        nueva_cadena_h = re.sub(homoclave, "", nueva_cadena_f)
        #print('homo')
        #print(validar_h)
        #print(nueva_cadena_h)
        vacio=['']
        transiciones=[]
        transiciones.extend(vacio)
        transiciones.extend(validar)
        transiciones.extend(validar_f)
        transiciones.extend(validar_h)

    return transiciones