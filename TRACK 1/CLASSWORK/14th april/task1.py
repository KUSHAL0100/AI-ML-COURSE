print("Enter your inputs 5 times")

i=0
evsum=0
odsum=0
sum=0
evcounter=0
odcounter=0
while i<5:
    n=int(input(f"Enter your input {i+1}: "))

    if n%2==0:
        evcounter+=1
        evsum+=n
    else:
        odcounter+=1
        odsum+=n
    i+=1
    sum+=n

print(f"Even counter is: {evcounter}")
print(f"Odd counter is: {odcounter}")
print(f"Even sum is: {evsum}")
print(f"Odd sum is: {odsum}")
print(f"Total sum is: {sum}")