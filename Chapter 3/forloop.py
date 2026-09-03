for i in range (10):
    print("hello world ")

#for loop for print 1 to 10  range is 1 to 11 

for i in range (1,11):
    print(f"hello world : {i}")




#Sum from 1-10
total = 0
i = 1
for i in range (1,21):
    print(f"Adding of value {i}")
    total += i
print(total)





# Through user input

n = int(input("Enter the number :- "))
total = 0
for i in range(1,n+1):
    # print(f"Value of {i}")
    total +=i
print(total)




#Calculate sum of digit 
total = 0
num = input("Enter a number :- ")
for i in range (0,len(num)):
    # print(f"Sum of {i}")
    total+=int(num[i])
print(total)




#ask user it his/her name and count each character 
# same character will not count 

name = input('Enter the name:-')
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}")
        temp+= name[i]