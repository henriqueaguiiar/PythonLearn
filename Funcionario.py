numFunc = int(input('Enter the employee id: '))
workHour = int(input('Enter number of worked hours: '))
valueWork = float(input('Enter the value of worked hour: '))

salary = float (workHour*valueWork)

print(f"NUMBER = {numFunc}\nSALARY = U$ {salary:.2f}")
