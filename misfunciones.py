def entero (a):
    """
    a esta función se le pasa un float o un string numérico y devuleve un entero.
    """
    return int(a)

def entero_if (a):
    """
    a esta función se le pasa un float o un string, se le compara si es numerico o no y si lo es devuelve se le pasa a int.
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