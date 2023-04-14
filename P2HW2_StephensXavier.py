# CTI-110
# P2HW2 - List
# Xavier Stephens
# 4/12/2023
#
mod1= float(input('Enter grade for module 1: '))
mod2= float(input('Enter grade for module 2: '))
mod3= float(input('Enter grade for module 3: '))
mod4= float(input('Enter grade for module 4: '))
mod5= float(input('Enter grade for module 5: '))
mod6= float(input('Enter grade for module 6: '))
print()
grades=[mod1, mod2, mod3, mod4, mod5, mod6]
low = min(grades)
high = max(grades)
total = sum(grades)
average = total / len(grades)

print('------------Results------------')
print(f'Lowest Grade:      {low:.1f}')
print(f'Highest Grade:     {high:.1f}')
print(f'Sum of Grades:     {total:.1f}')
print(f'Average:           {average:.2f}')
print('-----------------------------------------')
