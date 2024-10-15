def show_balance(balance):
    print(f"This is your balance: ${balance: .2f}")
def deposit_balance():
    amount = float(input("Please Enter Your Deposit Amount: "))
    if amount < 0:
        print("Deposit amount can't 0")
        return 0
    else:
        return amount
def withdraw_balance(balance):
    amount = float(input("Enter your Withdraw amount: "))
    if amount > balance:
        print("Insufficient Balance")
        return 0
    elif amount < 0:
        print("withdraw amount can't 0")
        return 0
    else:
        return amount
def main():
    balance =0 
    is_running = True

    while is_running:
        print("This BRAC Bank ATM")
        print("***************************************")
        print("1. Show Your Balance")
        print("2.Deposit Your Balance")
        print("3. Withdraw Your Balance")
        print("4.Exit")
        print()
        print("*******************************")

        choice = input("Please Enter your Choice: ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit_balance()
        elif choice == '3':
            balance -= withdraw_balance(balance)
        elif choice == "4":
            is_running = False
        else:
            print("This is not valid")

    print("Thanks for choose our ATM")

if __name__ == "__main__":
    main()