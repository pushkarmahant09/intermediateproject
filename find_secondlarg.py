tuple=[12,13,14,15,16,17]
y=0
second=0
largest=tuple[0]
while y<len(tuple):
    if tuple[y]>largest:
        second=largest
        largest=tuple[y]

    else:
        if tuple[y]>second and tuple[y]<largest:
            second=tuple[y]

    y+=1
print(second)

