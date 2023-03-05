bill = float(input("How much is the bill:\n"))
tip = float(input("The amount of tip you want to give 10, 12, or 15: "))
people = int(input("how many people are spliting the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
print("each person should pay:${a:1.2f}".format(a = bill_per_person))
