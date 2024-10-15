print("Assignment 1")

print("Exercise 1:")
print("")

# Ask for student's age
age = float(input("Enter your age:"))
if age > 18:
    # if age is greater than 18, they can proceed
    place = input("Enter your country:").strip().lower().replace(" ","")
    if place == "lebanon":
        # if location is "lebanon", they can proceed
        hk_score = float(input("Enter your HackerRank score:"))
        if hk_score > 110:
            # if hrScore is greater than , they are accepted
            print("Welcome to FCS!")
            # if the answers didn't meet the conditions
        else: 
            print("Insufficient Hacker Rank Score :(")
    else:
        print("Foreign Country")
else:
    print("Insufficient Age :(")

print("")
print("Exercise 2:")
print("")

n = int(input("Enter a random number: "))

if n%2 == 0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")
