# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:45:04 2022

@author: princ
"""
import re
import tkinter as tk
from tkinter import messagebox
from correo_main import diagrama_correo_electronico

#funciones
def CURP(curp):
    # Definimos la estructura de la CURP considerando las variaciones que presenta por medio de expresiones regulares, siendo un tanto similar a la del RFC
    patron = re.compile(
        "^[A-ZÑ]{1}(A|E|I|O|U|X)[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[0-9]|1[0-9]|2[0-9]|3[0-1])(H|M)(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)\w{5}")

    # Siempre que encuentre una coincidencia absoluta de nuestro patrón lo tomara como válido
    if (re.search(patron, curp)):
        print("CURP válida")

    else:
        print("CURP inválida")


def RFC_f(rfc):
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
        print("Direccion IP valida")
        ip_v=ip

    else:
        print("Dirección IP invalida")

    return(ip_v)


def FolioFiscal(folio_fiscal):
    # Dentro del patrón de expresiones regulares delimitamos los caracteres admitidos por los números hexadecimales
    patron = re.compile(
        "\w[0123456789abcdef]{1,8}[-]\w[0123456789abcdef]{1,4}[-]\w[0123456789abcdef]{1,4}[-]\w[0123456789abcdef]{1,4}[-]\w[0123456789abcdef]{1,12}")
    folio = patron.findall(folio_fiscal)

    aux = len(folio)

    # El auxiliar solo será mayor a cero si encuentra coinicdencia en la cadena ingresada por el usuario
    if aux > 0:
        print("Folio fiscal válido")
    else:
        print("Folio fiscal inválido")


def c_electronico(correo_electronico):
    correo = re.compile("\w+[@]\w+[.]\w+")
    comprobacion = correo.findall(correo_electronico)
    
    aux=len(comprobacion)
    
    if aux > 0:
        diagrama_correo_electronico(correo_electronico)

    else:
    	messagebox.showinfo(message="Correo electronico Invalido", title="Invalido")

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

