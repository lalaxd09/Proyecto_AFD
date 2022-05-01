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


    transicion=re.compile("^@")
    if (re.search(transicion, nueva_cadena)):
        transisicion_arroba=transicion.findall(nueva_cadena)
        nueva_cadena_t=re.sub(transicion, "", nueva_cadena)
        #print(transisicion_arroba)
        #print(nueva_cadena_t)

    compania=re.compile("^\w*")
    if (re.search(compania, nueva_cadena_t)):
        validar_c=compania.findall(nueva_cadena_t)
        nueva_cadena_c=re.sub(compania,"",nueva_cadena_t)
        #print(validar_c)
        #print(nueva_cadena_c)

    transcion_punto=re.compile("[.]\w+")
    if (re.search(transcion_punto, nueva_cadena_c)):
        validar_p=transcion_punto.findall(nueva_cadena_c)
        print(validar_p)
        #print(validar_p)
        #print(nueva_cadena_p)



    transciones=[]
    transciones.extend(validar)
    transciones.extend(transisicion_arroba)
    transciones.extend(validar_c)
    transciones.extend(validar_p)
    print(transciones)




    return transciones




