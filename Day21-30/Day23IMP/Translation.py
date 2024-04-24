FirstWord=input()
SecondWord=input()
Final=FirstWord[::-1]
if Final==SecondWord:
    print("YES")
else:
    print("NO")

# in this code i have learned a lot of thing it is not written in code but here they are 
# counter=1
# for i ,j in zip( range(0,len(FirstWord)) , range(len(FirstWord)-1,-1,-1) ):
#     if FirstWord[i]==SecondWord[j]:
#         counter=1
#     else:
#         counter=0
#         print("NO")
#         break
# if counter==1:
#     print("YES")
# here i have learned about zip and it is used to run two pointer for i and j simultaneously
# zip is taking two arguments first for i going from 0 to len(FirstWord) here last limit is not included 
# for example here word is code and len(FirstWord) will be 4 but range will go from to 3 
# for second range len(FirstWord) will be 4 but the indexing will start from 3 and go to 0 
# here as we know range do not include last range like we have written -1 why not 0 
# because it will not include -1 it will go upto 0 and third value -1 is steping value
# and one more inportant thing do not alway think about the looping please try to think for something constant