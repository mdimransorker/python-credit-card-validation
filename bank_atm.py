def show_balance():
    print(f"This is your balance: ${balance: .2f}")
def deposit_balance():
    amount = float(input("Please Enter Your Deposit Amount"))
    if amount < 0:
        print("Deposit amount can't 0")
        return 0
    else:
        return amount
def withdraw_balance():
    amount = float(input("Enter your Withdraw amount"))
    if amount > balance:
        print("Insufficient Balance")
        return 0
    elif amount < 0:
        print("withdraw amount can't 0")
        return 0
    else:
        return amount

balance =0 
is_running = True

while is_running:
    print("This BRAC Bank ATM")
    print("1. Show Your Balance")
    print("2.Deposit Your Balance")
    print("3. Withdraw Your Balance")
    print("4.Exit")

    choice = input("Please Enter your Choice")

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit_balance()
    elif choice == '3':
        withdraw_balance()
    elif choice == "4":
        is_running = False
    else:
        print("This is not valid")

print("Thanks for choose our ATM")