
# Python program to print positive Numbers in a List 
list = [12, -7, 5, 64, -14]  
num = 0
# using while loop      
while(num < len(list)):  
    if list[num] >= 0: 
        print(list[num],",", end = " ") 
    num += 1
