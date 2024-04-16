word=input()
First=word[0]
if ord(First) >= 65 and ord(First)<=90:
    print(word)
else:
    Final=chr(ord(First)-32)+word[1:]
    print(Final)
# this was easy question but i learned about ord and char and
# i was wrong for an instance like assigning the value to privious value
# i was getting an error here it is TypeError: 'str' object does not support item assignment
# i was doing like word[0]=char(ord(First)-32) it is not acceptable in python
# i have to do the of string and attach it to other string
# also first run all the test cases 
