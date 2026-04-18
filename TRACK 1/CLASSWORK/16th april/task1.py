n=int(input("Enter the number: "))

# for i in range(n,0,-1):
    # print(i)
evcnt=0
odcnt=0
evsum=0
odsum=0
totalsum=0
for i in range(1,n+1):
    if i%2==0:
        evcnt+=1
        evsum+=i
    else:
        odcnt+=1
        odsum+=i
    totalsum+=i

print(f"Even count is: {evcnt}")
print(f"Odd count is: {odcnt}")
print(f"Even sum is: {evsum}")
print(f"Odd sum is: {odsum}")
print(f"Total sum is: {totalsum}")

fact=1
for i in range(1,n+1):
    fact*=i

print(f"Factorial is: {fact}")
