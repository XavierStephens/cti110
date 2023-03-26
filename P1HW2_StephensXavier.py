#Homework
#3/26/23
#CTI-110 P1HW2- Travel Expense
#XavierStephens
#
print ('This program calculates and displays travel expenses')
print()
budget= int(input('Enter budget:'))
print()
destination= input('Enter your travel destination:')
print()
gas= int(input('How much do you think you will spend on gas?'))
print()
hotel= int(input('Approximately, how much will you need for accomodation/hotel?'))
print()
food= int(input('Last, how much do you need for food?'))
print()
print()
print('------------Travel Expenses------------')
print('Location:', destination)
print('Initial Budget:', budget)
print()
print('Fuel:', food)
print('Accomodation:', hotel)
print('Food:', food)
print()
expenses= gas+hotel+food
balance= budget-expenses
print('Remaining Balance:', balance) 
