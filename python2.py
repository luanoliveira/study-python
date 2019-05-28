# -*- coding: utf-8 -*-
from numbers import Number

numero = None

while numero==None:
    try:
        check = int(input("Enter something: "))
        numero = int(check)
    except ValueError:
        continue

print('O número informado foi ' + str(numero))
