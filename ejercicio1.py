#Ejercicio de matriz Juan David Rosero Torres 20181020071

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
for i in range(5):
    if(i==0):
        for a in range(3):
            print(str(matrix[0][a]))
    elif(i==1):
        for b in range(1,2):
            print(str(matrix[b][2]))
    elif (i==2):
        for c in range(2,0,-1):
            print(matrix[2][c])
    elif (i==3):
         for d in range(2,1,-1):
             print(matrix[d][0])
    elif(i==4):
        print(matrix[1][1])

    