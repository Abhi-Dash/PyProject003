# Take two input from the user and print the Quotient and Remainder
from argparse import REMAINDER

num_1 = int(input("Enter the First number: "))
num_2 = int(input("Enter the Second number: "))

Remainder = num_1%num_2
Quotient = num_1//num_2
print ("Quotient of given numbers is : ", Quotient)
print ("Remainder of given numbers is : ", Remainder)