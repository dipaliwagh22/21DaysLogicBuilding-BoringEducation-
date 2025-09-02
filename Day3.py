# determine if a user is eligible for a discount based on their membership status and purchase amount? 
# amount >=500--> eligible and status=True-->eligible
amount=float(input("Enter the purchase amount: "));
status=True
if status==True and amount>=500:
    print("Eligible for discount")
else:
    print("Not eligible for discount")