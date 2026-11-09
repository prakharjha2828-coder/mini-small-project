#Expense Tracker miniproject

expenseslist = [] #list of expenses in  from of dictionaries
print(" welecom to Expenes Tracker: Khrcha kam kiya kro")

while True:
    print("====Menu====")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice:")

#1.add Expense
    if( choice == "1"):
        date = input("Enter the date")
        category = input("Enter the category (Food,travel,books,other)")
        description = input("Enter all details of expense")
        amount = float(input("Emter the amount :"))

        expenses = {
            "date": date,
            "category": category,
            "description": description, 
            "amount": amount
        }
        expenseslist.append(expenses)
        print(" /n Done bro. Expense added successfully")
#2.view all expenses
    elif(choice == "2"):
        if(len(expenseslist) == 0):
            print("No expenses found. Go and spend some momey bro")
        else:
            print("All Expenses:")
            count = 1
            for  amount in expenseslist:
                print(f"spend money{count} :  -> {amount['date']},{amount['category']},{amount['description']}, {amount['amount']}")
                count += 1

#3.view total expenses
    elif(choice == "3"):
        total = 0
        for amount in expenseslist:
            total += amount['amount']
        print("/n Total amount : total")


#4. Exit
    elif(choice == "4"):
        print("Exiting the  system. Thank you for uising my expense tracker and  have a good day")
        break
    else:
        print("Invalid choice please try again")

            






