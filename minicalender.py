#Q1-to find the day with the date month year

date=int(input("enter the date-"))
while date>31 or date<1:
    print("Invalid date")
    date=int(input("enter the date again-"))

month=int(input("enter the month-"))
while month>12 or month<1:
    print("Invalid month")
    month=int(input("enter the month again-"))

year=int(input("enter the year-"))
while year<1899:
    print("Invalid year")
    year=int(input("enter the year again-"))


print(date,end=" -")
print(month,end=" - ")
print(year,end="  ")

y=0
sum=0
Months=[31,28,31,30,31,30,31,31,30,31,30,31]
if (year %4==0 and year%100!=0) or year %400==0 :
    # daysinyear=366
    Months[1]=29
    while y<month-1:
        sum=sum+Months[y]
        y+=1

else:
    # daysinyear=365

    while y<month-1:
        sum=sum+Months[y]
        y+=1

print(sum)
# print(daysinyear)
years_passed = year - 1900
leap_years = years_passed // 4 - years_passed // 100 + years_passed // 400
total_days = (years_passed * 365) + leap_years + sum + date


remaining_days=total_days%7

if remaining_days==0:
    print("Monday")
elif remaining_days==1:
    print("Tuesday")
elif remaining_days==2:
    print("Wednesday")
elif remaining_days==3:
    print("Thursday")
elif remaining_days==4:
    print("Friday")
elif remaining_days==5:
    print("Saturday")
elif remaining_days==6:
    print("Sunday")











