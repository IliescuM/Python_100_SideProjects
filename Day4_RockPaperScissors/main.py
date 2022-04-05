from calendar import c
import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# random_number = random_integer + random_float

# print(random_float)
# print(random_number)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score }")


# HEADS = 1
# TAILS = 2

# coin = random.randint(1, 2)
# if coin == HEADS:
#     print("Heads")
# else:
#     print("Tails")
# # random.choice(names) ptr o lista sa se aleaga random .

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

options = [rock, paper, scissors]

choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
while True:
    if choice < 0 or choice > 2:
        print("Invalid option.")
        choice = int(
            input(
                "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
            )
        )
    else:
        break

print(options[choice])
computer_choice = random.randint(0, 2)

print(f"Computer chose:\n {options[computer_choice]}")

# This can be done cleaner but for now it works.
if choice == 0 and computer_choice == 2:
    print("You win")
elif choice == 1 and computer_choice == 0:
    print("You win")
elif choice == 2 and computer_choice == 1:
    print("You win")
elif choice == 0 and computer_choice == 1:
    print("You lose")
elif choice == 1 and computer_choice == 2:
    print("You lose")
elif choice == 2 and computer_choice == 0:
    print("You lose")
elif choice == computer_choice:
    print("You draw")
