print("this pprogram show a example of if elif and nested if function")
amount=int(input("Enter The Price: "))
if amount>=200:
    discount=amount*0.05
    if amount>2000:
        discount=amount*0.25
elif amount>=500:
    discount=amount*0.10
elif amount>=1000:
    discount=amount*0.12
else:
    print("\nPlease Purchase",200-amount, "rupees of item to our shop")
netp=amount-discount    
print("\nDiscount: ",discount)
print("\nNet Payable amount",netp)

print("Thank You for Shoping with us")


    