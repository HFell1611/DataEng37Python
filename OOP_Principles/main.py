import cust
import employee
import random


if random.randint(0, 1) == 0:
    my_person = cust.Customer('Jyoti', 'Suresh', 'Mumbai')
else:
    my_person = employee.Employee('Minato', 'Fujiwara', 'Marketing')
my_person.print()
