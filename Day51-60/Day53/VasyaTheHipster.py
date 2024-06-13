RedSocks,BlueSlocks=map(int,input().split())
if RedSocks==min(RedSocks,BlueSlocks):
    LeftOver=BlueSlocks-RedSocks
    print(f"{RedSocks} {LeftOver//2}")
else:
    LeftOver=RedSocks-BlueSlocks
    print(f"{BlueSlocks} {LeftOver//2}")