String = "My name is Tushar"

print(String.replace(" ", "_")) #replace () method 
print(String.replace("is","was")) #repalce()method 


Name = "My name is Tushar and my surname is Behera"

print(Name.replace("is","was",1)) #only replace 1 st one 

print(Name.replace("is", "was",2)) # repalce both 


#find() Method

print(Name.find("is",1))


is_position1 = Name.find("is")
is_position2  = Name.find("is" , is_position1 + 1)
print(is_position2)


#Center method
# To make Our string in center like **Tushar**

Names = "Tushar"
print(Names.center(10 , "*"))


# Take input from user

Mobile = input("Enter Your Name :-")
print(name.center(len + 8 (Mobile) , "*"))