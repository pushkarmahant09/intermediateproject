str=input("enter the string")
y=0
count=0
while y<len(str):
    if str[y] in ["a","e","i","o","u"]:
        count+=1

    y+=1
if count>0:
        print("there are :",count,"vowels")

else:
    print("there are no vowels")

print(count)
