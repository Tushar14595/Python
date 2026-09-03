#Take two commmas seperated inputs from user
# 1. user name 
# 2. a single character 

# outputs

#user name length 
# count the character that user inputed


name,char = input("Enter your name and charcter seprated by comma :-") .split(",")


print(f"The total character is:- {len(name)}")
print(f"The total of a character is:- {name.lower().count(char.lower())}")

