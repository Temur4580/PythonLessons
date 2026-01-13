employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
result = f"{employee_list[1]}, {employee_list[-2]}"
print(result)

def dev_by_three(number):
    if number % 3 == 0:
         return 'Да'
    else:
         return 'Нет'

number_to_check = 10
result = dev_by_three(number_to_check)

print(f"Делится ли на три {number_to_check}? - {result}")

         