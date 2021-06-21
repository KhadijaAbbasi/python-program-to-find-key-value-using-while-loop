list=[]
i=0
while i<4:
    list.append(input('enter number: '))
    i=i+1
print(list)
key=input('Enter key value you want to search: ')
count=0
x=0
j=len(list)
while x<int(j):
    if int(key)==int(list[x]):
        count=count+1
    x=x+1
print(count)