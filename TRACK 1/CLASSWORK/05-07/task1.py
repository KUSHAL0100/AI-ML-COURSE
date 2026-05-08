
def rev(l,left,right):
    # 2 pointer approach for reverse
    while left<right:
        l[left],l[right]=l[right],l[left]
        left+=1
        right-=1
    print(l)

# print(l)
def pal(l,left,right):
    #2pointer approach for pallindrome
    ans="Yes"
    while left<right:
        if l[left]==l[right]:
            left+=1
            right-=1
        else:
            ans="No"
            break

    print(ans)


l=[1,2,3,2,10]

left=0
right=len(l)-1

pal(l,left,right)
rev(l,left,right)