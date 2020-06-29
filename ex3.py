print("I will now count my chickens")
print("Hens", 25+30/6)  # should be 30 decimal value
# remember the BODMAS rule of computers and heirarchy.. hence comes to be 97
print("Roosters", 100-25*3 % 4)
print("Now I will count the eggs")
# should be according to integers calculations and answer is 7 but comes out to be in decimal as all things in python turns out to be in decimal only... no concept or decimal and integer confusion like in java
print(3+2+1-5+4 % 2-1/4+6)  # comes to be 6/75
print("Is it true that 3+2 < 5-7")
print(3+2 < 5-7)  # obvious false and if it was only middle one it would be true
# here the relational signs held the last evaluation result and not the first
print("What is 3+2?", 3+2)
# enters space for the comma sign and not prints immediately
print("What is 5-7?", 5-7)
print("Oh thats why it is false")
print("how about some more?")
print("Is it greater", 5 > -2)
print("Is it greater than or equal to ", 5 >= -2)
print("Is it less than or equal to? ", 5 <= -2)


# order is in the form of PEMDAS
# actually it is PE(MD)(AS)

# parenthesis exponenets multiplication and division... addition and subtraction
