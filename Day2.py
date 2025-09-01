#  function for the age is eligible for voting or not

age = int(input("Enter your age: "))
def check_voting_eligibility(age):
    if age >= 18:
        print("Eligible for voting")
    else:
        print("Not eligible for voting")
check_voting_eligibility(age)
