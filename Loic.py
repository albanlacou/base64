def tab_to_string(tab_string):
    """
    return : string
    Rempli une string depuis un tableau
    """
    string = ""
    for i in tab_string :
        string = string + i
    return string


def fill_to_octet(string):
    """
    return : string
    Ajoute le nombre d'egal pour que le nombres de caractères soit un multiple de 8
    """
    nombre_tours = 0
    for i in string :
        nombre_tours = nombre_tours + 1
        print(nombre_tours)
    if nombre_tours % 8 != 0 :
        while nombre_tours % 8 != 0:
            nombre_tours = nombre_tours + 1
            string = string + "="
            print (string)
    return string





