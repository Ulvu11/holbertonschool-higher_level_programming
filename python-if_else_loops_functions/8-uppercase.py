#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Əgər simvol kiçik hərfdirsə (a-z arası)
        if ord(char) >= 97 and ord(char) <= 122:
            # ASCII kodundan 32 çıxaraq onu böyük hərfə çeviririk
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")  # Sonda yeni sətir üçün
