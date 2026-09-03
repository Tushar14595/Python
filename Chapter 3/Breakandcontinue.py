# to end the loop using the break keyword 


for i in range(1,11):
    # print(f"before break statement {i}")
    if i == 9:
        
        break
print(i)

# output
'''
before break statement 1
before break statement 2
before break statement 3
before break statement 4
before break statement 5
before break statement 6
before break statement 7
before break statement 8
before break statement 9
9
'''

# continue

#1to 10 series was print but not 5 in series 
# 1,2,3,4,6,7,8,9,10
for i in range(1,11):
    # print(f"before continue statement {i}")
    if i == 5:
        continue
    print(i)



# output
'''
1
2
3
4
6
7
8
9
10
'''