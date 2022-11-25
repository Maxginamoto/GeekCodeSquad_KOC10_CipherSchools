print("Welcome to the currency converter")
n="y"
while n=="y":
    a=input("Name the currency to be converted from: ")
    b=input("Name the currency to be converted into: ")
    c=int(input("Amount of "+a+" to be converted: "))
    d=float(input("How many "+b+" is one "+a+": "))
    print("That would be",c*d,b)
    n=input("Would you like continue??(y/n): ")
print("Thank you, This was made by: \n Sunidhi Tiwari(23)\n Mohak Khandelwal(24)\n Aryan Baloria(25)")
