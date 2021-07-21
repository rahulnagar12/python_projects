print("This programe is made for swaping the values which you enter.")
print('''\n\n There are Three mathods for swaping the values of two numbers
       in python. Inside the code you will see the all code as comment.''')
 
a=int(input("enter the first number: "))
b=int(input("enter the last number:"))

'''method first 

a_=a^b
b_=a^b
a_=a^b


method second:-
here we will use a tempary variable for storing temp value.
temp=a
a=b
b=temp

The last method is given below which work as main program
'''
A=a+b
B=A-b
A=A-B

print(A)
print(B)


print("\n\n The number you were enter %d and %d" %(a,b))
