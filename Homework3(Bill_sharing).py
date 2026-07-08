# Taking inputs
bill_total = float(input("Enter the total bill amount in ETB: "))
number_of_people = int(input("Enter the number of friends splitting the bill: "))

# 2. Write the function
def split_bill(total, people, tip_rate=0.10):
    total_with_tip = total * (1 + tip_rate)
    share_per_person = total_with_tip / people
    return share_per_person

# 3. Calling the function and storing it in a variable
individual_share = split_bill(bill_total, number_of_people)

# 4. Loop over a list of names and print each person's share
friends_list = []
print("\nEnter the names of your friends:")
for i in range(number_of_people):
    name = input(f"Friend {i+1} name: ")
    friends_list.append(name)

print("\n--- Final Split ---")
for friend in friends_list:
    print(f"{friend}'s share is: {individual_share:.2f} ETB")