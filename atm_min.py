username="Ruler"
password="Relur"

name=input("Enter your name: ")
passw=str(input("Enter your password: "))
if username==name and passw==password:
    print('''
            1.Deposit
            2.Cash Withdrawl   
            3.Ministatement
            4.Cancel Transaction
            ''')
    amount=100000
    option=int(input("Please select your option: "))
    if option==1:
        dep=int(input("Deposit your amount: "))
        amount+=dep
        print("Total amount:",amount)
    elif option==2:
        withd=int(input("Enter the amount: "))
        amount-=withd
        print("Total amount:",amount)
    elif option==3:
        print("******ATM******")
        print("username:",name)
        print("Total amount:",amount)
        print("***THANKING YOU***")
        print("--------------------")
else:
    print("please enter valid credentials")