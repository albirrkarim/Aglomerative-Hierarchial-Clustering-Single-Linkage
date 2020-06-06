# Aglomerative Hierarchial Clustering Single Linkage

def manhattan(arr1,arr2):
    return round(abs(arr1[0]-arr2[0])+abs(arr1[1]-arr2[1]),2)


def toMatrixDistance(data):

    out=[]

    for i in range(0,len(data)):

        row=[]
        for j in range(0,len(data)):
            distance = manhattan(data[i],data[j])

            row.append(distance)

        out.append(row)

    return out




data=[
    [0.40,0.53],
    [0.22,0.38],
    [0.35,0.32],
    [0.26,0.19],
    [0.08,0.41],
    [0.45,0.30],
]

o = toMatrixDistance(data)




# for i in o:

#     print(i)





def allMin(data):
    loca=[]
    a=data[0][0]
    for i in range(0,len(data)):

        for j in range(0,len(data)):
            if(a==0):
                a=data[i][j]
    
            elif( a > data[i][j] and data[i][j] !=0 ):
                a=data[i][j]
                loca=[a,i,j]

    return loca


k= allMin(o)

# print(k)

# def rmData(data,k):
#     a=k[1]
#     b=k[2]

#     out = []
#     for i in range(0,len(data)):
#         if(i!=a and i != b):
#             d = manhattan(data[a],data[i])
#             e = manhattan(data[b],data[i])

#             o = min([d,e])

            



def cok(data,row):
    out=[]
    for i in data:
        b = manhattan(i,row)

        out.append(b)

    return out





f= cok(data,data[k[1]])
g= cok(data,data[k[2]])

def giveMin(f,g):
    out=[]
    for i in range(0,len(f)):
        p = min([f[i] , g[i]])

        out.append(p)

    return out

x = giveMin(f,g)


# print(f)
# print(g)
# print(x)

# def makeNewMatrix()



data=[
    [0.40,0.53], #1
    [0.22,0.38], #2
    [0.35,0.32], #3
    [0.26,0.19], #4
    [0.08,0.41], #5
    [0.45,0.30], #6
]





col= [0,1,3,4]

for i in col:
    a = manhattan(data[i],data[2])
    b = manhattan(data[i],data[5])
    minus = min([a,b])
    # print(minus)

print("___________________________")

col= [0,3]

for i in col:
    a = manhattan(data[i],data[1])
    b = manhattan(data[i],data[4])
    minus = min([a,b])
    # print(minus)



P =[
    [2,4],
    [5,4],
    [3,4],
    [6,4],
  
]

out=[]
for i in P:
    a= manhattan(data[i[0]-1],data[i[1]-1])
    print("manhatan between ",i[0]," and ",i[1]," is ",a)
    out.append(a)

minus= min(out)

print("Terkecil adalah ",minus)