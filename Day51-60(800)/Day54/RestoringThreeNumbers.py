NumS=list(map(int,input().split()))
NumS.sort()
ABC=NumS[3]
AB=NumS[0]
AC=NumS[1]
BC=NumS[2]
print(f"{ABC-BC} {ABC-AC} {ABC-AB}")
