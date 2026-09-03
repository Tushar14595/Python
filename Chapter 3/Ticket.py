age =  input("Enter your age :- ")
age = int(age)

if age == 0 or age < 0:
 print("You can't watch")
elif 1 < age <= 3:
 print("Ticket price : free")
elif 3 < age <= 10:
 print("Ticket price : 150")
elif 10 < age<= 60:
 print("Ticket price : 250")
else:
 print("Ticket price: 200")