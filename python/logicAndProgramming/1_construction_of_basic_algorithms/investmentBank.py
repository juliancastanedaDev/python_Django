#!/usr/bin/env python

"""
    Interest earned on investment in a monthly bank
    investment = the amount to be invested by the client in the bank
    n = Interest percentage offered by the bank
    interests = value that the client will earn in pesos
    totalValue = value of the interest plus the value of the investment
"""

investment = int(input("Ingrese el valor de su inversión "))
n = int(input("ingrese el porcentaje ofrecido por el banco "))
interests = investment * (n / 100)
totalValue = investment + interests
print("El valor de sus intereses mensuales seria ${} Pesos".format(interests))
print("El valor total al mes de su inversion sería ${} pesos.".format(totalValue))

