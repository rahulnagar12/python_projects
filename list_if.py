thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("Please enter only lowercase")
entry=input("\nEnter a fruite name: ")
if "apple" in thislist:
    print("The fruit apple is in our database")
elif "banana" in thislist:
    print("The fruit banana is in our database")
elif "cherry" in thislist:
    print("The fruit cherry is in our database")
elif "orange" in thislist:
    print("The fruit orange is in our database")
elif "kiwi" in thislist:
    print("The fruit kiwi is in our database")
elif "melon" in thislist:
    print("The fruit melon is in our database")
elif "mango" in thislist:
    print("The fruit mango is in our database")
else:
    print("The fruit is not in our database")