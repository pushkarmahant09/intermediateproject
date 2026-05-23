# # this is the small atm machine structure .Just make for fun
x = 0
balance = 0
y = 0

cv = int(input("enter your last four atm digit- "))
pin = int(input("enter your pin- "))

data = {
    9867: 1234,
    9245: 9009
}

if cv in data:

    if pin == data[cv]:

        print("pin corrected")
        print("Welcome Back.........\n")

    else:

        # 3 ATTEMPT LOGIN SYSTEM
        for i in range(1, 4):

            pin = int(input("enter your pin again- "))

            if pin == data[cv]:

                print("pin corrected")
                print("Welcome Back.........\n")
                break

        else:

            print("incorrect pin entered")
            print("try again later")


    # ENTER ATM ONLY IF PIN IS CORRECT
    if pin == data[cv]:

        while True:

            print("\n========ATM MENU=========")
            print("1-DEPOSIT")
            print("2-CHECK BALANCE")
            print("3-WITHDRAW")
            print("4-EXIT\n")

            choice = int(input("SIR,WHAT DO YOU WANT "))


            if choice == 1:

                x = int(input("enter money-----"))

                if x > 1000000:

                    print("Amount too big")

                else:

                    balance = balance + x
                    print(x, "is deposited")


            elif choice == 2:

                print("AVAILABLE BALANCE-", balance)


            elif choice == 3:

                y = int(input("ENTER AMOUNT-"))

                if y > balance:

                    print("INVALID AMOUNT")

                else:

                    print(y, "AMOUNT WITHDRAWN")

                    balance = balance - y
                    print("AVAILABLE BALANCE-", balance)


            elif choice == 4:

                print("THANK YOU(..)")
                break


            else:

                print("Invalid Choice")

else:

    print("Invalid username")