
def string_to_array(text):
    tab = []
    for i in text:
        tab.append(i)
    return tab

def string_to_ascii(string_tab):
    tab = []
    for i in string_tab:
        tab.append(ord(i))
    return tab

def ascii_to_hex(ascii_tab):
    tab= []
    for i in ascii_tab:
        binaire = bin(i)
        tab.append(binaire[2:])
    return tab

def bin_to_octet(hex_tab):
    tab=[]
    for i in hex_tab:
        if len(i) != 7:
            





tab = string_to_array("ABCD")
tab = string_to_ascii(tab)

tab = ascii_to_hex(tab)
print(tab)