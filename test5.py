"5.	Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them. Examples 1,3 ➞ 3780, 2,0 ➞ 7200"
hours = int(input("number 1 "))
minutes= int(input("number 2 "))
secondsHour=hours*3600
secondsMinutes=minutes*60
result=secondsHour+secondsMinutes
print(result)