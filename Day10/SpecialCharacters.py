size=int(input())
for i in range(size):
    Num=int(input())
    if Num%2==0 and Num!=0:
        print("YES")
        Arr=[0]*Num
        Char='A'
        for j in range(Num):
            if j%2==0:
                # print(j,j+1)
                if Char=="A":
                    Char="B"
                else:
                    Char="A"
                Arr[j]=Char
                Arr[j+1]=Char
            else:
                pass
        print("".join(Arr))
    else:
        print("NO")
# In this I have to think about changing character every time and i have learned about join
# this problem was bit difficult to understand I was unable to understand by test cases 
# You can tak help of YT to understand the question
# first we have checked if the under can have neighbour i mean even number can have neighbour but odd can't
# Example 2 AA and 3 AAA or AABA in case of 3 we can't have three special character it could be 4 or 2
# so we have checked if number is even or not than we have proceed 