# Voter and Membership Eligibility Checker
def main():
    # Step 1: Get user input for age and citizenship
    age = int(input("Enter your age: "))
    citizenship = input("Enter your country of citizenship: ").capitalize()

    # Step 2: Check voting eligibility using decision structures and logical operators
    if age >= 18 and citizenship == "USA":
        print("You are eligible to vote in the USA.")
    elif age >= 18:
        print(f"You are eligible to vote in {citizenship}.")
    else:
        print("You are too young to vote.")

    # Step 3: Check for club membership using a Boolean variable
    is_member = input("Are you a club member? (yes/no): ").lower()
    membership_status = (is_member == "yes")  # Boolean variable for membership status

    if membership_status:
        print("Welcome to the club!")
    else:
        print("You need to be a member to access the club.")

    # Step 4: Perform additional decision-making using nested if statements
    if membership_status:
        print("Enjoy exclusive benefits as a club member!")
        if age < 30:
            print("You qualify for a youth member discount.")
        else:
            print("You qualify for a senior member discount.")
    else:
        print("Sign up today to enjoy membership benefits!")

# Calling the main function to run the program
if __name__ == "__main__":
    main()
