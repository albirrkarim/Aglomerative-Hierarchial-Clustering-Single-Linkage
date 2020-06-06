# Aglomerative Hierarchial Clustering Single Linkage
# by Al Birr Karim Susanto

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


def manhattanCounter(data,twoPoint):
    print("\n\nCounting manhattan distance between two point")
    out=[]
    for i in twoPoint:
        a = manhattan(data[i[0]-1],data[i[1]-1])
        print("Manhatan between ",i[0]," and ",i[1]," is ",a)
        out.append(a)

    minus = min(out)
    print("The smallest one is ",minus)
    return minus


def allMin(data):
    print("Search smallest value from matrix, return [small,idxOfRow,idxOfColumn]")
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




data=[
    [0.40,0.53], #1
    [0.22,0.38], #2
    [0.35,0.32], #3
    [0.26,0.19], #4
    [0.08,0.41], #5
    [0.45,0.30], #6
]

mtr = toMatrixDistance(data)
smallest = allMin(mtr)

print(smallest)

twoPoint =[
    [2,4],
    [5,4],
    [3,4],
    [6,4], 
]

manhattanCounter(data,twoPoint)