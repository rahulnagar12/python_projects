print("this pprogram show a example of if elif and nested if function")
amount=int(input("\nEnter The Price: "))
if amount>=200:
    discount=amount*0.05
    netp=amount-discount 
    print("\nDiscount: ",discount)
    print("\nNet Payable amount",netp)
    print("\n")
    print("\n")
    print("\n")
    print("Thank You for Shoping with us")
    if amount>2000:
        discount=amount*0.25
        netp=amount-discount 
        print("\nDiscount: ",discount)
        print("\nNet Payable amount",netp)
        print("\n")
        print("\n")
        print("\n")
        print("Thank You for Shoping with us")
elif amount>=500:
    discount=amount*0.10
    netp=amount-discount 
    print("\nDiscount: ",discount)
    print("\nNet Payable amount",netp)
    print("\n")
    print("\n")
    print("\n")
    print("Thank You for Shoping with us")
elif amount>=1000:
    discount=amount*0.12
    netp=amount-discount 
    print("\nDiscount: ",discount)
    print("\nNet Payable amount",netp)
    print("\n")
    print("\n")
    print("\n")
    print("Thank You for Shoping with us")
else:
    print("\nPlease Purchase",200-amount, "rupees of item to our shop")   


