#-----------------------Credit card validator in python-------------------------

#1. Remove any '_' or ' ' 
# 2. Add all digits in the odd places from right to left 
# 3. Double every second digit from right to left. 
#    ( If result is a two-digit number, 
#     add the two-digit number together to get a single digit) 
# 4. Sum the totals of step 2 & 3 
# 5. If sum is divisible by 10, the credit card #is valid

sum_odd_digits = 0
sum_even_digits = 0
total = 0

#step 1

card_number = input("Enter your credit card number #: ")
card_number = card_number.replace("-","" )
card_number = card_number.replace(" ", "")
card_number = card_number[:: -1]
print(card_number)