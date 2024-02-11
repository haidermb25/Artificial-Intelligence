
#Task:2
data1=list()
#Here we take 10 inputs
for i in range(0,10):
   value1=int(input(f"Enter the {i+1} number: "))
   data1.append(value1)

for i in range(0,10):
    if data1[i]%2==0:
        print("%d is Even"  %data1[i])
    else:
        print("%d is Odd" %data1[i])
