def tab_to_string(tab_string):
    """return : string
    fill a string with a table
    """
    string = ""
    for i in tab_string:
        string = string + i
    return string


def fill_to_octet(string):
    """return : string
    Add an egal number for caracters numbers be a multiple of 8
    """
    nombre_tours = 0
    for i in string:
        nombre_tours = nombre_tours + 1
    if nombre_tours % 8 != 0:
        while nombre_tours % 8 != 0:
            nombre_tours = nombre_tours + 1
            string = string + "="
    return string