#ask user to input a number containing more than one digit.
# example  = 1256
# calculate 1+2+5+6 and print


# algorithm - (method to solve in human language)
# ask input in string, don't change string to int 
# eg - "1256"
# pick a string character one by one and change to int
# int(example[0]) + int(example[1]) .............. go up to len(example)

number = input("Enter the digit at least four:- ")
i =1
while i <= number:
    i+=int(i)
print(i)
