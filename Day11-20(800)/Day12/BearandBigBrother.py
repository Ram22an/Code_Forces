counter=0
limak,Bob=map(int,input().split())
if limak == Bob:
    print(1)
else:
    while True:
        counter=counter+1
        Bob=Bob*2
        limak=limak*3
        # print(limak,Bob,counter)
        if limak>Bob:
            print(counter)
            break

# here is also a learning please read the question properly