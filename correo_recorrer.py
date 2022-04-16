import re


#c=c_electronico(correo)

#re.compile("\w+[@]\w+[.]\w+")
def datos_automata(correo):
    inicio=re.compile("^\w*")
    if (re.search(inicio, correo)):
        validar=inicio.findall(correo)
        nueva_cadena=re.sub(inicio,"",correo)
        #print(validar)
        #print(nueva_cadena)
    else:
        print("Vuelva a ingresar el correo")


    transicion=re.compile("[@]")
    if (re.search(transicion, nueva_cadena)):
        transisicion_arroba=inicio.findall(nueva_cadena)
        nueva_cadena_t=re.sub(transicion, "", nueva_cadena)
        #print(transisicion_arroba)
        #print(nueva_cadena_t)

    compañia=re.compile("^\w*")
    if (re.search(compañia, nueva_cadena_t)):
        validar_c=inicio.findall(nueva_cadena_t)
        nueva_cadena_c=re.sub(compañia,"",nueva_cadena_t)
        #print(validar_c)
        #print(nueva_cadena_c)

    transcion_punto=re.compile("[.]")
    if (re.search(transcion_punto, nueva_cadena_c)):
        validar_p=inicio.findall(nueva_cadena_c)
        nueva_cadena_p=re.sub(transcion_punto,"",nueva_cadena_c)
        #print(validar_p)
        #print(nueva_cadena_p)

    extension=re.compile("^\w*")
    if (re.search(extension,nueva_cadena_p)):
        validar_e=extension.findall(nueva_cadena_p)
        nueva_cadena_e=re.sub(extension,"",nueva_cadena_p)
        #print(validar_e)
        #print(nueva_cadena_e)

    estados=[]
    estados.extend(validar)
    estados.extend(validar_c)
    estados.extend(validar_e)
    #print(estados)

    transiciones=['@','.']


    return estados,transiciones




