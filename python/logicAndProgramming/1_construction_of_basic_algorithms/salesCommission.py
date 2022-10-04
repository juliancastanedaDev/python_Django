#!/usr/bin/env python


"""
    A seller receives a base salary plus an extra 10% commission on his sales,
    the seller wants to know how much money he will get as commissions for the
    three sales he makes in the month and the total he will receive in the month
    taking into account his salary basis and commissions.
    salary = base salary
    sales = amount of sales to calculate the commission
    totalCommissions = Additional 10% for each sale
    totalSalary = Base salary plus commissions
"""

salary = int(input("Ingrese su Salario "))
sales = int(input("Ingrese el total de ventas del mes para calcular su comisión "))
totalCommissions = (salary * 0.10) * sales
totalSalary = salary + totalCommissions
print ("El total de sus comisiones es ${}".format(totalCommissions))
print ("El total de su salario con comisiones incluidas es de ${}".format(totalSalary))
