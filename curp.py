import re
from funcion import CURP
"""Curp 
^[A-ZÑ]{1}(A|E|I|O|U|X)[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[0-9]|1[0-9]|2[0-9]|3[0-1])(H|M)(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[A-Z]{4}[0-9]{1}")
"""
def curp_datos(curp):
    transicion_pa = re.compile("^(([A-ZÑ]{1})(A|E|I|O|U|X)([A-Z]{2}))")
    if (re.search(transicion_pa, curp)):
        transisicion_apel = transicion_pa.findall(curp)
        #print(transisicion_apel)
        n=[]
        for i in transisicion_apel:
            new=i[0]
            n.append((new))
       #(n)
        nueva_cadena_apellid = re.sub(transicion_pa, "", curp)

    #transicion_vocal=re.compile("A|E|I|O|U|X [A-Z]{2}")
    """if (re.search(transicion_vocal, nueva_cadena_apellid)):
        transisicion_v = transicion_vocal.findall(nueva_cadena_apellid)
    
        nueva_cadena_v = re.sub(transicion_vocal, "", nueva_cadena_apellid)"""





    transicion_n = re.compile("^(([0-9]{2})(0[1-9]|1[0-2])(0[0-9]|1[0-9]|2[0-9]|3[0-1]))")
    if (re.search(transicion_n, nueva_cadena_apellid)):
        transisicion_new = transicion_n.findall(nueva_cadena_apellid)
        #print(transisicion_new)
        nueva_cadena_n = re.sub(transicion_n, "", nueva_cadena_apellid)
        transisicion_new_c=[]
        for y in transisicion_new:
            nn=y[0]
            transisicion_new_c.append(nn)
        #print(transisicion_new_c)


    transisicion_s=re.compile("^H|M")
    if (re.search(transisicion_s, nueva_cadena_n)):
        transisicion_sexo = transisicion_s.findall(nueva_cadena_n)
        #print(transisicion_sexo)
        nueva_cadena_sexp = re.sub(transisicion_s, "", nueva_cadena_n)

    transisicion_e=re.compile("^AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE")
    if (re.search(transisicion_e, nueva_cadena_sexp)):
        transisicion_entidad = transisicion_e.findall(nueva_cadena_sexp)
        #print(transisicion_entidad)
        nueva_cadena_entidad = re.sub(transisicion_e, "", nueva_cadena_sexp)

    transicion_h=re.compile("^[A-Z]{4}[0-9]{1}")
    if (re.search(transicion_h, nueva_cadena_entidad)):
        transisicion_homo = transicion_h.findall(nueva_cadena_entidad)
        #print(transisicion_homo)
        nueva_cadena_homo = re.sub(transicion_h, "", nueva_cadena_entidad)


    vacio=['']
    transiciones=[]
    transiciones.extend(vacio)
    transiciones.extend(n)
    transiciones.extend(transisicion_new_c)
    transiciones.extend(transisicion_sexo)
    transiciones.extend(transisicion_entidad)
    transiciones.extend(transisicion_homo)

    return transiciones


