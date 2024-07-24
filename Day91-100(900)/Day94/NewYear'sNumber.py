x = int(input())
for _ in range(x):
    num = int(input())
    found = False
    for i in range(num // 2021 + 1):
        if (num - 2021 * i) % 2020 == 0:
            found = True
            break
    if found:
        print("YES")
    else:
        print("NO")
# here we finding if a number after subtracting 2021 with power of i
# and then diving it with 2020 is giving 2020 if true then yess otherwise no
