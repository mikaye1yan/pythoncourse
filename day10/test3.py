def days(month, year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29
    return days_in_month[month - 1]
print(days(2, 2018))   
print(days(4, 654))    
print(days(2, 200))   
print(days(2, 1000))   
