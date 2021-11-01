import re
import pandas as pd
def entero (a):
    """
    a esta función se le pasa un float o un string numérico y devuleve un entero.
    """
    return int(a)

def entero_if (a):
    """
    a esta función se le pasa un float o un string
    mira si el string es númerico, y si lo es lo convierte a int
    si no lo es devuleve la cadena
    """
    if a.isdigit():
        return int(a)
    else:
        return a

def cambia (a):
    """
    recibe una lista y un número
    cada elemento de la lista lo cambia por el número recibido
    """
    return a


def edades (col):
    """
    recibe un string
    si contiene "months" devuelve el string tal cual
    si contiene un número de uno o dos dígitos devuelve el número
    si no contiene números devuelve el string en función del contenido del primero
    """
    if re.findall(".*months",col):
        return col
    elif re.findall("\d{1,2}",col):
        return re.findall("\d{1,2}",col)[0]
    elif re.findall(".*oung",col):
        return "25"
    elif re.findall(".*dul",col):
        return "35"
    elif re.findall(".*teen",col):
        return "15"
    elif re.findall(".*lder",col):
        return "75"
    elif re.findall(".*iddle",col):
        return "50"
    else:
        return "UNKNOWN"

def actividades (col):
    """
    recibe un string 
    devuelve strings en función del contenido del recibido
    """
    if re.findall(".*[Uu](NKNOW|nknow).*",col):
        return "Unknown"                  
    elif re.findall(".*o injury.*",col):
        return "No injury"
    elif re.findall(".*[Ff](ATAL|atal).*",col):
        return "Fatal injury"
    elif re.findall(".*[Bb](itten|ITTEN).*",col):
        return "Bitten"
    elif re.findall(".*[Ll](acerat|ACERAT).*",col):
        return "Lacerations"
    elif re.findall(".*[Mm](inor|INOR).*",col):
        return "Minor injuries"
    elif re.findall(".*[Ss](EVERED|evered).*",col):
        return "Limb severed"
    elif re.findall(".*[Pp](unctur|UNCTUR).*",col):
        return "Punctured"
    elif re.findall(".*[Ii](njur|NJUR).*",col):
        return "Injured"                  
    elif re.findall(".*o detai.*",col):
        return "No details"
    else:
        return "Others"