from tabulate import tabulate
import math
import random
import copy


def fitnessfunction(a, b, c, d):
    fitnessfunction_ans = 100 * (b - a**2)**2 + (1 - a)**2 + 90 * (d - c**2)**2 + (1 - c)**2 + 10.1 * ((b - 1)**2 + (d - 1)**2) + 19.8 * (b - 1) * (d - 1)
    return fitnessfunction_ans

def getrandomnumber(a,b):
    randnum = random.uniform(a,b)
    ans = round(randnum,6)
    return ans

x_all = ["x1","x2","x3","x4"]


Problist_Value = [[0]*2 for _ in range(20)]
Problist = [[0]*2 for _ in range(20)]
X_Value = [[0]*4 for _ in range(20)]
fitnessfunction_X_Value =  [ [0] for _ in range(20) ]

TotalProb_Value = 0
Chosen_Prob_Org = 0
Chosen_Prob = 0
ans = 9999999


for i in range(20):

    x1 = getrandomnumber(-10,10)
    x2 = getrandomnumber(-10,10)
    x3 = getrandomnumber(-10,10)
    x4 = getrandomnumber(-10,10)

    X_Value[i][0] = x1
    X_Value[i][1] = x2
    X_Value[i][2] = x3 
    X_Value[i][3] = x4

    Chosen_Prob_Org = fitnessfunction(x1,x2,x3,x4)
    Chosen_Prob_Org = float(format(Chosen_Prob_Org, '.6f'))
    TotalProb_Value += Chosen_Prob_Org
    TotalProb_Value = float(format(TotalProb_Value,'.6f'))
    Problist_Value[i][0] = Chosen_Prob_Org
    Problist_Value[i][1] = TotalProb_Value

    fitnessfunction_X_Value[i] = fitnessfunction(x1,x2,x3,x4) #計算fitnessfunction
    X_Value[i].append(fitnessfunction_X_Value[i])

fitnessfunction_X1_Value = copy.deepcopy(fitnessfunction_X_Value) #計算fitnessfunction

for _ in range(1000):

    for i in range(20):
        Problist[i][0] = round(Problist_Value[i][0] / Problist_Value[19][1],10)
        Chosen_Prob += Problist[i][0]
        Problist[i][1] += round(Chosen_Prob,1)


        # ---------輪盤法----------

        circle = [ [ 0 ] * 2 for _ in range(20)]

        for k in range(20):
            
            count = 0

            #random  number between 0 and 1, and the    precision number is 6
            RandomToComp_base = random.uniform(0,1)
            RandomToComp = round(RandomToComp_base,6)
            
            for j in range(20):
                if( Problist[j][1] < RandomToComp ):
                    count+=1
                elif(Problist[j][1] > RandomToComp):
                    circle[i][0] = i
                    circle[i][1] = count+1
                    break

        # print(circle)

        # ----------輪盤法----------

        # ----------交叉----------

        crossover_array = []

        for i in range(20):
                
            RandomToComp = float(format(random.uniform(0,1), '.6f'))
            if(RandomToComp < 0.7):
                crossover_array.append(1)
            else:
                crossover_array.append(0)

        crossover_array1 = []
        for i in range(20):
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
            X1_Value[crossover_array1[counter2]][3] = B*X_Tmp_Value[crossover_array1[0]][3] + (1-B) * X_Tmp_Value[crossover_array1[1]][3]

            X1_Value[crossover_array1[counter2+1]][0] = (1-B)*X_Tmp_Value[crossover_array1[0]][0] + B * X_Tmp_Value[crossover_array1[1]][0]
            X1_Value[crossover_array1[counter2+1]][1] = (1-B)*X_Tmp_Value[crossover_array1[0]][1] + B * X_Tmp_Value[crossover_array1[1]][1]
            X1_Value[crossover_array1[counter2+1]][2] = (1-B)*X_Tmp_Value[crossover_array1[0]][2] + B * X_Tmp_Value[crossover_array1[1]][2]
            X1_Value[crossover_array1[counter2+1]][3] = (1-B)*X_Tmp_Value[crossover_array1[0]][3] + B * X_Tmp_Value[crossover_array1[1]][3]
            counter2 += 2

        for i in range(20):
            X1_Value[i][4] = fitnessfunction(X1_Value[i][0], X1_Value[i][1], X1_Value[i][2], X1_Value[i][3])

        # print(tabulate(X1_Value,headers=x_all))
        # ----------交叉----------

        # ----------突變----------


        MutationRate = 0.1

        for i in range(20):
            MutationRandom = getrandomnumber(0,1)

            if(MutationRandom < MutationRate):

                X_Tmp_Value[i][0] = getrandomnumber(-10,10)
                X_Tmp_Value[i][1] = getrandomnumber(-10,10)
                X_Tmp_Value[i][2] = getrandomnumber(-10,10)
                X_Tmp_Value[i][3] = getrandomnumber(-10,10)
            X_Tmp_fitnessfunction = fitnessfunction(X_Tmp_Value[i][0], X_Tmp_Value[i][1], X_Tmp_Value[i][2], X_Tmp_Value[i][3])
            X_Tmp_Value[i][4] = (X_Tmp_fitnessfunction)

        # ----------突變----------

        # for i in range(20):
        #     for j in range(20):
        #         if(X_Value[i][4] > X1_Value[i][4]):
        #             X_Value[i][0],X1_Value[i][0] = X1_Value[i][0],X_Value[i][0]
        #         if(X_Value[i][4] > X_Tmp_Value[i][4]):
        #             X_Value[i][0],X_Tmp_Value[i] = X_Tmp_Value[i],X_Value[i]

        
        # for i in range(20):
        #     if(X_Value[i][4] > X1_Value[i][4]):
        #         for j in range(5):
        #             X_Value[i][j],X1_Value[i][j] = X1_Value[i][j],X_Value[i][j]
        #     if(X_Value[i][4] > X1_Value[i][4]):
        #         for j in range(5):
        #             X_Value[i][j],X_Tmp_Value[i][j] = X_Value[i][j],X_Tmp_Value[i][j]

        # ans_i = 0
        # for i in range(20):
        #     if(X_Value[i][4] <= ans):
        #         ans = X_Value[i][4]
        #         ans_i = i
        for j in range(20):
            for k in range(20):
                if (X_Value[j][4]>X1_Value[k][4]):
                    for p in range(5):
                        X_Value[j][p],X1_Value[k][p] = X1_Value[k][p],X_Value[j][p]
                if (X_Value[j][4]>X_Tmp_Value[k][4]):
                    for p in range(5):
                        X_Value[j][p],X_Tmp_Value[k][p] = X_Tmp_Value[k][p],X_Value[j][p]

    # print(tabulate(X_Value[ans_i]))
    print(tabulate(X_Value,numalign='left',tablefmt='plain'))



# print(tabulate(Problist,numalign='left',tablefmt='plain'))
# print("--------------------")
# print(Problist_Value)
# print("---------------")
# print(Problist)