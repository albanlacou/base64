def tab_to_string(tab_string):
    string = ""
    for i in tab_string :
        string = string + i
    return string

def fill_to_octet(string):
    nombre_tours = 0
    for i in string :
        nombre_tours = nombre_tours + 1
        print(nombre_tours)
    if nombre_tours < 8 :
        for i in string :
            string = string + "="
            print(string)
        return string