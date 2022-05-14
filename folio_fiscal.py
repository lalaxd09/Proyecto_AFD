import re
from funcion import FolioFiscal


# "\w[0123456789abcdef]{1,8}[-]\w[0123456789abcdef]{1,4}[-]\w[0123456789abcdef]{1,4}[-]\w[0123456789abcdef]{1,4}[-]\w[0123456789abcdef]{1,12}")
def f_f(folio):
    inicio = re.compile("^\w[0123456789ABCDEF]{1,8}")
    if (re.search(inicio, folio)):
        validar = inicio.findall(folio)
        #print(validar)
        nueva_cadena = re.sub(inicio, "", folio)

    guion = re.compile("^[-]")
    if (re.search(guion, nueva_cadena)):
        validar_g = guion.findall(nueva_cadena)
        #print(validar_g)
        nueva_cadena_g = re.sub(guion, "", nueva_cadena)
        print(nueva_cadena_g)

    segundo = re.compile("^\w[0123456789ABCDEF]{1,4}")
    if (re.search(segundo, nueva_cadena_g)):
        validar_s = segundo.findall(nueva_cadena_g)
        nueva_cadena_s = re.sub(segundo, "", nueva_cadena_g)
        #print(nueva_cadena_s)

    guion_s = re.compile("^[-]")
    if (re.search(guion_s, nueva_cadena_s)):
        validar_gs = guion_s.findall(nueva_cadena_s)
        nueva_cadena_gs = re.sub(guion_s, "", nueva_cadena_s)
        #print(nueva_cadena_gs)

    tercero = re.compile("^\w[0123456789ABCDEF]{1,4}")
    if (re.search(tercero, nueva_cadena_gs)):
        validar_t = tercero.findall(nueva_cadena_gs)
        nueva_cadena_t = re.sub(tercero, "", nueva_cadena_gs)

    guio_t= re.compile("^[-]")
    if (re.search(guio_t, nueva_cadena_t)):
        validar_guiot = guio_t.findall(nueva_cadena_t)
        nueva_cadena_guiot = re.sub(guio_t, "", nueva_cadena_t)

    cuarto= re.compile("^\w[0123456789ABCDEF]{1,4}")
    if (re.search(cuarto, nueva_cadena_guiot)):
        validar_ct = cuarto.findall(nueva_cadena_guiot)
        nueva_cadena_ct = re.sub(cuarto, "", nueva_cadena_guiot)

    guio_q= re.compile("^[-]")
    if (re.search(guio_q, nueva_cadena_ct)):
        validar_guioq = guio_q.findall(nueva_cadena_ct)
        nueva_cadena_guioq = re.sub(guio_q, "", nueva_cadena_ct)

    quinto= re.compile("^\w[0123456789ABCDEF]{1,12}")
    if (re.search(quinto, nueva_cadena_guioq)):
        validar_q = quinto.findall(nueva_cadena_guioq)
        nueva_cadena_q = re.sub(quinto, "", nueva_cadena_guioq)

    vacio=['']
    transicion=[]
    transicion.extend(vacio)
    transicion.extend(validar)
    transicion.extend(validar_g)
    transicion.extend(validar_s)
    transicion.extend(validar_gs)
    transicion.extend(validar_t)
    transicion.extend(validar_guiot)
    transicion.extend(validar_ct)
    transicion.extend(validar_guioq)
    transicion.extend(validar_q)

    return transicion