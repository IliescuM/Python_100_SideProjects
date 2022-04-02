import string


print("``` Welcome to the tip calculator ```\n")
total_bill = input("~ What was the total bill? $")
number_people = input("~ How many people to split the bill? ")

percentage_tip = input("~ What percentage tip would you like to give? 10, 12, or 15? ")
if not (
    int(percentage_tip) == 10 or int(percentage_tip) == 12 or int(percentage_tip) == 15
):
    while True:

        if not (
            int(percentage_tip) == 10
            or int(percentage_tip) == 12
            or int(percentage_tip) == 15
        ):
            print("~ Invalid tip percentage ! \n")
            percentage_tip = input(
                "~ What percentage tip would you like to give? 10, 12, or 15? "
            )
        break


result = float(total_bill) / float(number_people) + float(total_bill) / float(
    number_people
) * (float(percentage_tip) / 100)
result = round(result, 1)

print("~ Each person should pay: $" + str(result))
