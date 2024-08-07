import sys
# def check_lines(lines):
#     for line in lines:
#         if line.count("B") == 8:
#             return "B"
#         elif line.count("R") == 8:
#             return "R"
#     return None
def check_columns(grid):
    for col in range(8):
        if all(grid[row][col] == 'B' for row in range(8)):
            return "B"
    return None
t = int(input().strip())
for _ in range(t):
    # got to know about new thing 
    # input_data = sys.stdin.read()
    # lines = input_data.strip().split('\n')
    # this is used for taking input
    input()
    grid = [input().strip() for _ in range(8)]
    for line in grid:
        if line.count("R") == 8:
            print("R")
            break
    else:
        result = check_columns(grid)
        if result:
            print(result)
    # result = check_lines(grid)
    # if result:
    #     print(result)
    #     continue
    # rotated = [['' for _ in range(8)] for _ in range(8)]
    # for r in range(8):
    #     for c in range(8):
    #         rotated[c][8 - 1 - r] = grid[r][c]
    
    # result = check_lines(rotated)
    # if result:
    #     print(result)
# it is also not considered as mine because logic was mine like checking for count of r in rows and
# checking for b in coloumns and if equal to 8 then print it and i know that there is count function
# so i though of using it but i have implemented the code with chatgpt so it is not mine
# i am thinking about copying the code from chat gpt is not good for my code forces journey
# because i am trying to do question but they are started to getting out of my league and copying it is cheating 
# i think i should stop psoting question every day and do the dsa and logic building and continue my 
# journey after some time this will cost me my streak on code forces
# for now good bye and see you soon with more questions
