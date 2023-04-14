#CTI-110
#P3HW2 - Salary
#Xavier Stephens
#4/13/2023
#
emp_name = input('Enter employees name: ')
hours_worked = int(input('Enter number of hours worked: '))
pay_rate = float(input('Enter employees pay rate: '))
if hours_worked > 40:
    ot_hours = hours_worked - 40
    ot_pay = (pay_rate * 1.5) * ot_hours
    reg_hour_pay = pay_rate * 40
else:
    ot_hours = 0
    ot_pay = 0
    reg_hour_pay = pay_rate * hours_worked
gross_pay = reg_hour_pay + ot_pay

print(f'-----------------------------------------')
print(f'Employee name:   {emp_name}')
print()
print(f'Hours Worked   Pay Rate   OverTime   Overtime Pay    RegHour Pay    Gross Pay')
print(f'------------------------------------------------------------------------------------')
print(f'{hours_worked:.1f}           ${pay_rate:.2f}     {ot_hours:.1f}        ${ot_pay:.2f}          ${reg_hour_pay:.2f}        ${gross_pay:.2f}')
