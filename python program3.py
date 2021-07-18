#PYTHON PROGRAM TO PRINT POSITIVE NUMBERS IN A LIST 

List = []

Number = int(input("Enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of %d Element : " %i))
    List.append(value)

print("\nPositive Numbers in this List are : ")
for j in range(Number):
    if(List[j] >= 0):
        print(List[j], end = '   ')
