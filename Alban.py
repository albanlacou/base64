import Loic
base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlmnopqrstuvwxyz0123456789+/"


def string_to_array(text):
    """ return an array
     convert a string to an array
     """
    tab = []
    for i in text:
        tab.append(i)
    return tab

def string_to_ascii(string_tab):
    """ return an array
    convert a string array to ascii array
    """
    tab = []
    for i in string_tab:
        tab.append(ord(i))
    return tab

def ascii_to_hex(ascii_tab):
    """ return an array
    convert a ascii array to hexadecimal array
    """
    tab= []
    for i in ascii_tab:
        binaire = bin(i)
        tab.append(binaire[2:])
    return tab

def hex_to_bin(hex_tab):
    """ return an array
    convert a decimal array to binairie array
    """
    tab=[]
    for i in hex_tab:
        if len(i) != 8:

            tab.append(i.zfill(8))
        else:
            tab.append(i)
    return tab

def cut_every_six_character(bin_tab):
    """ return an array
    cut a string every six character
    """
    tab = []
    text = Loic.tab_to_string(bin_tab)

    x = 0
    while x+6 <= len(text):
        tab.append(text[x:x+6])
        x += 6
    tab.append(text[x:len(text)].zfill(6))
    return tab

def hex_to_decimal(hex_tab):
    """ return an array
    convert a hexadecimal array to ascii array
    """
    tab = []
    for i in hex_tab:
        tab.append(int(i,2))
    return tab


def decimal_to_char(decimal_tab):
    """ return an array
    convert a hexadecimal array to character array
    """
    tab= []
    for i in decimal_tab:
        tab.append(base64[i])
    return tab


tab = string_to_array("ABCD")
tab = string_to_ascii(tab)

tab = ascii_to_hex(tab)
tab = hex_to_bin(tab)
tab = cut_every_six_character(tab)
tab = hex_to_decimal(tab)
tab = decimal_to_char(tab)
print(tab)