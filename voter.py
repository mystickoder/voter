print("Hello Welcome to Voter Precinct One")

age = int(input("How old are you? "))
if age >= 21:
    print('You are old enough to vote. ')
    
elif age <= 21:
    print("You are not old enough to vote. ")

if age >= 21:
    print("Here is your ballot please proceed to the next booth.")
    
if age <= 21:
    print("Please return when you are 21.")
    
print("Thanks for visiting  Voter Precinct One")
    