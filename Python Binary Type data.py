"""Python Binary Type Data """
"""Frist kno list ka byte ba bytearray ta convert korte hobe, byte data change kota jai na onno dike bytearray data 
change kora jai """
list1=[1,2,3,4,5,6,7,8,8,9,122,133,144,155,166,177,188,199,200,211,222,233,244,255]
byteconvert=bytes(list1)
print(byteconvert)
print(type(byteconvert))
byteconvert[0]=100
#