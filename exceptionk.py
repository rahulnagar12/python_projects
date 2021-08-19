# This is a foultfull calculater only in division opration
num1 = int(input("Plese enter a number: "))
num2 = int(input("Plese enter next number: "))

print("\nNOTE:- if you try to division 2 number it will always take big number as number A")

print('''\nChose a number :
1 addition
2 division
3 multiplication
4 min(-)
''')
opp = int(input("choose a number only: "))
try:
    if opp == 1:
        Total = num1+num2
        print("Total: ", Total)

    if opp == 2:
        Total = num1/num2
        if num1 < num2:
            Total = num2/num1
        print("Total: ", Total)

    if opp == 3:
        Total = num1*num2
        print("Total: ", Total)

    if opp == 4:
        Total = num1-num2
        print("Total: ", Total)

except ZeroDivisionError:
    print("you can not divide a nuber with Zero",)

except ValueError as e:
    print("Please input the right key words", e)

except Exception as arrr:
    print("Something Wrong", arrr)

finally:
    print("BYE BYE")
    print("Thank You For Yousing")





