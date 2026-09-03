# WATCh - COCO movie
# Ask user Age and Name 
# If user name start with ("a" or "A") and age is above 10
# print you can watch coco movie
# else sorry, u can't watch 



name = input("Enter your name:")
age = int(input("Enter your age:"))
if age<=10:
 print(f"Hello {name} You can watch coco movie")
else:
 print(f"Sorry, {name} you can't watch ")