#Declarated matrix's before the code, simulating static vectors
#Challenge of my teacher. The homework has the limitation of using
#Static list, and ignore that python only haves dynamic vectors.

#Codigo en ingles por que quiero subir cosas a mi Github que lo tengo re vacio

#Correccion a un error.
mat=[[0]*10]*10
horiz=[[0]*10]*10
diag=[0] * 10
vert=[[0]*10]*10
diag2=[0]*10
sumh=[0]*10
sumv=[0]*10

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
sumd=0
sumd2=0
#Exercise says that we have to do a Magic Matrix on a Cuadrate matrix with dimensions specified by the user.
#This also has a limit, we have to set this limit to 10, due to the limitation of simulating static vectors.
#(Limit was chosen by the teacher)
while Bucle:
    #Reinicio sumas
    sumh = [0] * 10
    sumv = [0] * 10
    sumd = 0
    sumd2 = 0
    valid=True
    correct=True
    try:
        dims=int(input("Write the matrix dimensions. Limit is ten. "))
    except ValueError:
        print("Only numbers are allowed, please write it again.")
        correct=False
    #try:
    if correct == True and dims < 11:
        for i in range(0,dims):
            #Profe hay que ponerlo aca si o si a este vector por un tema de como funciona la asignacion con *
            #This have to be here with no option by how works the vectors assignation with *
            nums = [0] * 10
            for j in range(0,dims):
                nums[j]=int(input("Write a number. Sudoku bro "))
            #print("ROW "+str(i)+" Completed whit values:"+str(nums))
            mat[i] = nums
        for i in range(0,dims):
            vert[i]=[fila[i] for fila in mat]
        horiz=mat

        for i in range(0,dims):
            diag[i]=vert[i][i]
        for i in range(dims-1,-1,-1):
            diag2[dims-1-i]=vert[i][dims-i-1]
        #print(vert)
        #print(horiz)
        #print(diag)
        #print(diag2)
        for i in range(0,dims):
            for j in range(0,dims):
                sumv[i]=sumv[i]+vert[i][j]
                sumh[i]=sumh[i]+horiz[i][j]
        for i in range(0,dims):
            sumd=sumd+diag[i]
            sumd2=sumd2+diag2[i]
        #print(sumv)
        #print(sumh)
        #print(sumd)
        #print(sumd2)
        for i in range(0,dims):
            if sumv[i]==sumh[i] and sumv[i]==sumd and sumv[i]==sumd2:
                pass
            else:
                valid=False
        if valid:
            print("THIS IS A MAGIC MATRIX WHAAAAAAAAAAAT!!!!!!!!!!!!!!!!")
        else:
            print("THIS ISNT A MAGIC MATRIX NOOB L+RATIO+GG+EZ")
   # except:
    #    print("Algo salio mal / Something went wrong.")


