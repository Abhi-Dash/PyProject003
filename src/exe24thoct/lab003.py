# Write a program that calculates and displays the letter grade for a given numerical score
# (e.g., A, B, C, D, or F) based on the following grading scale:

# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59

x = int(input("Enter a Number: "))
if 90<=x<=100:
    print ("The value is A ")
elif 80<=x<=89:
    print("The value is B")
elif 70<=x<=79:
    print("The value is C")
elif 60<=x<=69:
    print("the value is D")
elif 0<=x<=59:
    print("The value is F")
else:
    print ("Invalid Number\nPlease enter a number in between 0 to 100")

