#Homework
#4/12/23
#CTI-110 P2HW1- Travel 
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
print(f'Location:          {destination}')
print(f'Initial Budget:    ${budget:.1f}')
print(f'Fuel:              ${food:.1f}')
print(f'Accomodation:      ${hotel:.1f}')
print(f'Food:              ${food:.1f}')
print('---------------------------------------')
print()
expenses= gas+hotel+food
balance= budget-expenses
print(f'Remaining Balance: ${balance:.1f}') 
