Polyhedrons={"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20} 
FinalCount=0
NumberOfPolyhedrons=int(input())
for i in range(NumberOfPolyhedrons):
    TypeOfPolyhedrons=input()
    FinalCount=Polyhedrons[TypeOfPolyhedrons]+FinalCount
print(FinalCount)
# here we have learned about dictionary 