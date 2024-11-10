#Leap Year Checker:

year = int (input("Enter any year to check : "))
if (year%4==0 and year%100 !=0) or (year%400==0):
    print("{} Year is a leap year".format(year))
else:
    print ("{} year is not a leap year".format(year))