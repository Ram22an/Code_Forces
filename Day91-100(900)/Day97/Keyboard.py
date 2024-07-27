TOTALDict={'q': [-1, 'w'], 'w': ['q', 'e'], 'e': ['w', 'r'], 'r': ['e', 't'], 't': ['r', 'y'], 'y': ['t', 'u'], 'u': ['y', 'i'], 'i': ['u', 'o'], 'o': ['i', 'p'], 'p': ['o', -1],'a': [-1, 's'], 's': ['a', 'd'], 'd': ['s', 'f'], 'f': ['d', 'g'], 'g': ['f', 'h'], 'h': ['g', 'j'], 'j': ['h', 'k'], 'k': ['j', 'l'], 'l': ['k', ';'], ';': ['l', -1],'z': [-1, 'x'], 'x': ['z', 'c'], 'c': ['x', 'v'], 'v': ['c', 'b'], 'b': ['v', 'n'], 'n': ['b', 'm'], 'm': ['n', ','], ',': ['m', '.'], '.': [',', '/'], '/': ['.', -1]}
Choice=input()
Str=input()
RightOrLeft = 1 if Choice == "L" else 0
# this is same as done below
# RightOrLeft=-1
# if Choice=="L":
#     RightOrLeft=1
# else:
#     RightOrLeft=0
Ans=""
for i in Str:
    if i in TOTALDict and TOTALDict[i][RightOrLeft]!=-1:
        Ans+=TOTALDict[i][RightOrLeft]
print(Ans)
# this is my appraoch and this is working and accepted but i don't like this appraoch
# here is the code that i found on chatgpt and it is good first i was trying to find the logic for the
# placement of the key in keyboard but i thought it is random to slow down the person and prevent typewritter to jam
# but we can make logic for this also by simple way 
# this is how i have got the TOTALDict not the exact but some what
keyboard = [
    "qwertyuiop",
    "asdfghjkl;",
    "zxcvbnm,./"
]
# here we have taken the rows from keyboard
Choice = input().strip()
Str = input().strip()
# here we are getting shift by checking r or l 
shift = -1 if Choice == "R" else 1  # Shift means R means we are taking the right char of current char
# it is simple as if else
Ans = ""

for char in Str:
    # we are getting char from the input string
    for row in keyboard:
        # then we are comparing char with rows if it is present in it
        if char in row:
            # if true
            index = row.index(char)
            # getting index 
            new_index = index + shift
            # getting new char index
            Ans += row[new_index]
            # adding it to answer
            break
print(Ans)
# it was simple question but by first reading i thought i was not able to do this
