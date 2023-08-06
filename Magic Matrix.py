#Declarated matrix's before the code, simulating static vectors
#Challenge of my teacher. The homework has the limitation of using
#Static list, and ignore that python only haves dynamic vectors.

#Codigo en ingles por que quiero subir cosas a mi Github que lo tengo re vacio

mat=[[0]*10 for i in range(10)]
guardSum=[0 for i in range(22)]

#Variables
#Specifies the type by the exersice rules my teacher said.
#boolean
Bucle=True
valid= True
#integger
dims=0
#boolean
correct=True
cont = 0
cuantoRestar=0
#Exercise says that we have to do a Magic Matrix on a Cuadrate matrix with dimensions specified by the user.
#This also has a limit, we have to set this limit to 10, due to the limitation of simulating static vectors.
#(Limit was chosen by the teacher)
while Bucle:
    cuantoRestar=0
    guardSum=[0]*10
    valid=True
    correct=True
    try:
        dims=int(input("Write the matrix dimensions. Limit is ten. "))
    except ValueError:
        print("Only numbers are allowed, please write it again.")
        correct=False
    if correct == True and dims < 11:
        try:
            for i in range(0,dims):
                for j in range(0,dims):
                    mat[i][j]=int(input("Write a number. Sudoku bro "))
        except ValueError:
            print("Only numbers are allowed, please start again.")
        #print("ROW "+str(i)+" Completed whit values:"+str(mat))
        if correct==True:
            #Filas
            for i in range(0,dims):
                for j in range(0,dims):
                    guardSum[i]=guardSum[i]+mat[j][i]
            #Columnas
            for i in range(dims,dims*2):
                for j in range(0,dims):
                    guardSum[i]=guardSum[i]+mat[i-dims][j]
            #Primer diagonal
            for i in range(0,dims):
                guardSum[dims*2]=guardSum[dims*2]+mat[i][i]
            #Segunda diagonal
            for i in range(dims,-1,-1):
                guardSum[dims*2+1]=guardSum[dims*2+1]+mat[i][i]
            for i in range(1,dims*2+1):
                if guardSum[i]!=guardSum[i-1]:
                    valid=False
            if valid:
                print("THIS IS A MAGIC MATRIX WHAAAAAAAAAAAAAAAAAAAAAAAT!!!!!!!!")
            else:
                print("THIS ISNT MAGIC LOL BRO HAHA L + NOOB + RATIO + EZ")
            print("Las sumas son: ")
            print("Filas: ",end="")
            for i in range(0, dims):
                print(str(guardSum[i]),end=", ")
            print("\nColumnas: ",end="")
            for i in range(dims, dims * 2):
                print(str(guardSum[i]),end=", ")
            print("\nPrimer diagonal: "+ str(guardSum[dims*2]))
            print("Segunda diagonal: "+ str(guardSum[dims*2+1]))
            #print(guardSum)
    elif dims>10:
        print("WTF BRO? I TOLD YOU THAT THE LIMIT IS TEN, WRITE IT AGAIN.")



