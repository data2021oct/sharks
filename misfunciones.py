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