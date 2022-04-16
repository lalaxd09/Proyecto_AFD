# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:45:04 2022

@author: princ
"""
import re
#funciones
def CURPS(curp):

    
    patron=re.compile("^[A-ZÑ]{1}(A|E|I|O|U|X)[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[0-9]|1[0-9]|2[0-9]|3[0-1])(H|M)(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[A-Z]{4}[0-9]{1}")


    if (re.search(patron, curp)):
        print("Curp Valida")
    else:
        print("Curp Invalida")
    


def RFC(rfc):
    patron=re.compile("^([A-ZÑ\x26]{3,4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1]))([A-Z\d]{3})?$")

    if (re.search(patron, rfc)):
        print("RFC valida")
        
    else:
        print("RFC Invalida")

def Validate_web(web):
 
    # Regex expression
    regex = "^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$"

     
    p = re.compile(regex)

    if (re.search(p, web)):
        return "Direccion WEB valida"
 
    return "Dirección WEB invalida"



def Validate_ip(ip):
 
    # Regex expression
    regex = "(([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
            "2[0-4][0-9]|25[0-5])\\.){3}"\
            "([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
            "2[0-4][0-9]|25[0-5])"

     
    p = re.compile(regex)

    if (re.search(p, ip)):
        return "Direccion IP valida"
 
    return "Dirección IP invalida"

def correo_fiscal(folio_fiscal):
    patron = re.compile("\w[0123456789abcdef]{1,8}[-]\w[0123456789abcdef]{1,4}[-]\w[0123456789abcdef]{1,4}[-]\w[0123456789abcdef]{1,4}[-]\w[0123456789abcdef]{1,12}")
    folio=patron.findall(folio_fiscal)
    
    #cadenas de prueba
    #folio=patron.findall("a98fdc10-c145-4520-6324-fabc467ec035")
    #folio=patron.findall("a98fgc10-c145-4520-6324-flbc467ec035")
    
    aux=len(folio)
    
    if aux > 0:
    	print("Folio fiscal valido")
    else:
    	print("Folio fiscal invalido")
    
        
    
def c_electronico(correo_electronico):
    correo = re.compile("\w+[@]\w+[.]\w+")
    comprobacion = correo.findall(correo_electronico)
    
    aux=len(comprobacion)
    
    if aux > 0:
    	print("correo electronico valido")
    else:
    	print("correo electronico invalido")

    return correo
        
def hour(hora):
    patron= re.compile("\d{1,2}[h]|\d{1,2}[:]\d{1,2}")

    if (re.search(patron, hora)):
        return "Hora valida"
 
    
    return "Hora invalida"

def fecha(date):
    patron= re.compile("\d{1,2}[/]\d{1,2}[/]\d{1,4}")

    if (re.search(patron, date)):
        return "Fecha valida"
 
    return "Fecha invalida"

