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
    ascii_tab = []
    for i in string_tab:
        ascii_tab.append(ord(i))
    return ascii_tab


def ascii_to_hex(ascii_tab):
    """ return an array
    convert a ascii array to hexadecimal array
    """
    hexadecima_tab = []
    for i in ascii_tab:
        binairy = bin(i)
        hexadecima_tab.append(binairy[2:])
    return hexadecima_tab


def hex_to_bin(hex_tab):
    """ return an array
    convert a decimal array to binairy array
    """
    binary = []
    for i in hex_tab:
        if len(i) != 8:

            binary.append(i.zfill(8))
        else:
            binary.append(i)
    return binary


def cut_every_six_character(bin_tab):
    """ return an array
    cut a string every six character
    """
    six_character_tab = []
    text = Loic.tab_to_string(bin_tab)

    x = 0
    while x + 6 <= len(text):
        six_character_tab.append(text[x:x + 6])
        x += 6
    six_character_tab.append(text[x:len(text)].zfill(6))
    return six_character_tab


def hex_to_decimal(hex_tab):
    """ return an array
    convert a hexadecimal array to ascii array
    """
    decimal_tab = []
    for i in hex_tab:
        decimal_tab.append(int(i, 2))
    return decimal_tab


def decimal_to_char(decimal_tab):
    """ return an array
    convert a hexadecimal array to character array
    """
    char_tab = []
    for i in decimal_tab:
        char_tab.append(base64[i])
    return char_tab


tab = string_to_array("ABCD")
tab = string_to_ascii(tab)

tab = ascii_to_hex(tab)
tab = hex_to_bin(tab)
tab = cut_every_six_character(tab)
tab = hex_to_decimal(tab)
tab = decimal_to_char(tab)
string = Loic.tab_to_string(tab)
string = Loic.fill_to_octet(string)
print(string)
