from tabulate import tabulate
import math
import random
import copy

population_size = 20


def fitnessfunction(a, b, c):
    return a + b + c

def getrandomnumber(a,b):
    randnum = random.uniform(a,b)
    ans = round(randnum,4)
    return ans

x_all = ["x1","x2","x3","x4","x5","x6","x7","x8"]

Problist_Value = [[0]*2 for _ in range(population_size)]
Problist = [[0]*2 for _ in range(population_size)]
X_Value = [[0]*8 for _ in range(population_size)]
fitnessfunction_X_Value =  [ [0] for _ in range(population_size) ]

TotalProb_Value = 0
Chosen_Prob_Org = 0
Chosen_Prob = 0
ans = 9999999

for i in range(population_size):

    for k in range(999999999):
        x1 = getrandomnumber(100,10000)
        x2 = getrandomnumber(1000,10000)
        x3 = getrandomnumber(1000,10000)
        x4 = getrandomnumber(10,1000)
        x5 = getrandomnumber(10,1000)
        x6 = getrandomnumber(10,1000)
        x7 = getrandomnumber(10,1000)
        x8 = getrandomnumber(10,1000)
    
    
        if(x4 + x6 <= 400 and x5 + x7 - x4 <= 400 and x8 - x5 <= 100 and x1 * x6 - 833.33252 * x4 -100 * x1 + 83333.333 >= 0) == True:
            if(x3 * x8 - 1250000 - x3 * x5 + 2500 * x5 >= 0 and x2 * x7 - 1250 * x5 - x2 * x4 + 1250 * x4 >= 0) == True:
                X_Value[i][0] = x1
                X_Value[i][1] = x2
                X_Value[i][2] = x3
                X_Value[i][3] = x4
                X_Value[i][4] = x5
                X_Value[i][5] = x6
                X_Value[i][6] = x7
                X_Value[i][7] = x8
                print("i and k is ",i,k)
                break

    Chosen_Prob_Org = fitnessfunction(x1,x2,x3)
    Chosen_Prob_Org = float(format(Chosen_Prob_Org, '.4f'))
    TotalProb_Value += Chosen_Prob_Org
    TotalProb_Value = float(format(TotalProb_Value,'.4f'))
    Problist_Value[i][0] = Chosen_Prob_Org
    Problist_Value[i][1] = TotalProb_Value

    fitnessfunction_X_Value[i] = fitnessfunction(x1,x2,x3) #計算fitnessfunction
    X_Value[i].append(fitnessfunction_X_Value[i])

fitnessfunction_X1_Value = copy.deepcopy(fitnessfunction_X_Value) #計算fitnessfunction

print(tabulate(X_Value))

for i in range(1):

    for i in range(population_size):
        Problist[i][0] = round(Problist_Value[i][0] / Problist_Value[19][1],10)
        Chosen_Prob += Problist[i][0]
        Problist[i][1] += round(Chosen_Prob,1)


        # ---------輪盤法----------

        circle = [ [ 0 ] * 2 for _ in range(population_size)]

        for i in range(population_size):
            
            count = 0

            #random  number between 0 and 1, and the    precision number is 6
            RandomToComp_base = random.uniform(0,1)
            RandomToComp = round(RandomToComp_base,4)
            
            for j in range(population_size):
                if( Problist[j][1] < RandomToComp ):
                    count+=1
                elif(Problist[j][1] > RandomToComp):
                    circle[i][0] = i
                    circle[i][1] = count+1
                    break

        # ----------輪盤法----------

        # ----------交叉----------

        crossover_array = []

        for i in range(population_size):
                
            RandomToComp = float(format(random.uniform(0,1), '.4f'))
            if(RandomToComp < 0.7):
                crossover_array.append(1)
            else:
                crossover_array.append(0)

        crossover_array1 = []
        for i in range(population_size):
            if(crossover_array[i]==1):
                crossover_array1.append(i)

        counter1 = 0

        for nunbers in crossover_array1:
            counter1 += 1

        if(counter1 % 2 == 1):
            counter1  -= 1

        counter1 = int(counter1 / 2 )
        counter2=0


        X1_Value = copy.deepcopy(X_Value) #設為交叉後的值
        X_Tmp_Value = copy.deepcopy(X_Value) #拿來當作暫存值& 突變時被拿來覆蓋

        for i in range(counter1):
            B = getrandomnumber(0.001,0.009)
            
            X1_Value[crossover_array1[counter2]][0] = B*X_Tmp_Value[crossover_array1[0]][0] + (1-B) * X_Tmp_Value[crossover_array1[1]][0]
            X1_Value[crossover_array1[counter2]][1] = B*X_Tmp_Value[crossover_array1[0]][1] + (1-B) * X_Tmp_Value[crossover_array1[1]][1]
            X1_Value[crossover_array1[counter2]][2] = B*X_Tmp_Value[crossover_array1[0]][2] + (1-B) * X_Tmp_Value[crossover_array1[1]][2]

            X1_Value[crossover_array1[counter2+1]][0] = (1-B)*X_Tmp_Value[crossover_array1[0]][0] + B * X_Tmp_Value[crossover_array1[1]][0]
            X1_Value[crossover_array1[counter2+1]][1] = (1-B)*X_Tmp_Value[crossover_array1[0]][1] + B * X_Tmp_Value[crossover_array1[1]][1]
            X1_Value[crossover_array1[counter2+1]][2] = (1-B)*X_Tmp_Value[crossover_array1[0]][2] + B * X_Tmp_Value[crossover_array1[1]][2]
            counter2 += 2

        for i in range(population_size):
            X1_Value[i][3] = fitnessfunction(X1_Value[i][0], X1_Value[i][1], X1_Value[i][2])

        # print(tabulate(X1_Value,headers=x_all))
        # ----------交叉----------

        # ----------突變----------


        MutationRate = 0.1

        for i in range(population_size):
            MutationRandom = getrandomnumber(0,1)

            if(MutationRandom < MutationRate):

                X_Tmp_Value[i][0] = getrandomnumber(-10,10)
                X_Tmp_Value[i][1] = getrandomnumber(-10,10)
                X_Tmp_Value[i][2] = getrandomnumber(-10,10)
            X_Tmp_fitnessfunction = fitnessfunction(X_Tmp_Value[i][0], X_Tmp_Value[i][1], X_Tmp_Value[i][2])
            X_Tmp_Value[i][3] = (X_Tmp_fitnessfunction)

        # ----------突變----------

        for j in range(population_size):
            for k in range(population_size):
                if (X_Value[j][4]>X1_Value[k][4]):
                    for p in range(5):
                        X_Value[j][p],X1_Value[k][p] = X1_Value[k][p],X_Value[j][p]
                if (X_Value[j][4]>X_Tmp_Value[k][4]):
                    for p in range(5):
                        X_Value[j][p],X_Tmp_Value[k][p] = X_Tmp_Value[k][p],X_Value[j][p]
    #print(tabulate(X_Value,numalign='left',tablefmt='plain'))


