stock={"APPLE":200,"TSLA":250,"GOOGLE":500,"BMW":100}
total=0
while True:
    product=input("Enter product name:").upper()
    quantity=int(input("Enter quantity:"))
    found=False
    for a in stock:
        if product==a:
            found=True
            price=stock[a]*quantity
            total=total+price
            print(f"total of {a} is {price}:")
    if found==False:
        print("Product not found.")
    print(f"total so far is:{total}")
    ask_for_another_stock=input("Do you want to check another stock?y/n ")
    if ask_for_another_stock=="n":

        break

print("-------Your Portfolio-----------")
print("Total Investment:",total)
print("Thank you for using Stock portfolio Tracker!")




