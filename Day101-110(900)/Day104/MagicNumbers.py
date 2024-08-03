def CheckingMagic(num):
    i = 0
    n = len(num)
    while i < n:
        if num[i] == '1':
            if i+2 < n and num[i:i+3] == '144':
                i += 3
            elif i+1 < n and num[i:i+2] == '14':
                i += 2
            else:
                i += 1
        else:
            print("NO")
            return
    
    print("YES")
    return

# it was my pervious logic and it was quite close to correct one but i was not handling the correct way 
    # check=False
    # temp=["2", "3", "5", "6", "7", "8", "9", "0"]
    # if num[0]!="1":
    #     print("NO")
    #     return
    # for i in range(0,len(num)-3,4):
    #     if num[i]=="1":
    #         if num[i:i+2]=="14":
    #             if num[i:i+3]=="144":
    #                 check=True
    #             check=True
    #         check=True
    #     else:
    #         check=False
    #         break
    # if check:
    #     print("YES")
    #     return
    # else:
    #     print("NO")
    #     return
num = input().strip()
CheckingMagic(num)
