Mishka = 0
Chris = 0
x = int(input())
for _ in range(x):
    M, C = map(int, input().split())
    if M > C:
        Mishka += 1
    elif C > M:
        Chris += 1
if Mishka > Chris:
    print("Mishka")
elif Chris > Mishka:
    print("Chris")
else:
    print("Friendship is magic!^^")
# in this first we have to see who win the most number of rounds
# not the total
# at first i was check the total not the number os rounds
