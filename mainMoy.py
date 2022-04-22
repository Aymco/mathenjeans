import math
import matplotlib.pyplot as plt

proba = []
probaX = []
X= []
Y = []
print("ok")


def formuleBrute(listC, T):
    for i in range(T):
        value = listC[T-i-1]
        if(i!=0):
            #transition diagonale
            listC[T-i] += value * (i+1)

        #transition verticale
        listC[T-i-1] = value * (T-i-0)
            
    return (listC)

def main():
    _input = int(input("#Types de cartes : "))
    for i in range(1):
        T = (i + 1) * _input
        
        listCalcul = [0] * T
        #plt.plot(T-1, 0, 'bo', lw=3)
        listCalcul[0] = 1
        tirees = 2
        probaInt = 0

        #proba.append(0)
        #probaX.append(0)
        #proba.append(0)
        #probaX.append(1)

        esperance = 0
        proba = 0

        while 100 * proba <= 99:

            precProba = proba
            listCalcul = formuleBrute(listCalcul, T)
            proba = listCalcul[T - 1] / T ** (tirees)
            p = (proba - precProba)
            print(p)
            esperance += tirees * p

            tirees += 1


        print(str(T) + " cartes: Espérance: " + str(esperance))
        

'''
        while 100 * probaInt <= 99 * T ** (tirees - 1):

            listCalcul = formuleBrute(listCalcul, T)
             #print(listCalcul)
            probaInt = listCalcul[T - 1]
            p = (100 * probaInt / T ** (tirees))
            if(tirees%50 == 0):
                print( str(tirees)+  "  " +  str(p).replace(".", ","))
            proba.append(p)
            probaX.append(tirees)


            tirees += 1
        print(str(tirees) + " : " +  str(p))
        print(str(T) + " : " + str(tirees - 1))
        X.append(T)
        Y.append(tirees - 1)
        plt.plot(probaX, proba,  lw=2, label=str(T))
        proba.clear()
        probaX.clear()
    #print(proba)





    plt.title('Probabilité pour ' + str(T) + ' cartes')
    plt.xlabel('Nombre de cartes tirées')
    plt.ylabel('Probabilité')
    plt.legend()
    plt.grid(True)
    plt.show()
'''

'''
        for i in range(20):

            # on verifie par echelle de 5% la probabilite
            while 20 * probaInt <= i * T ** (tirees - 1):


                probaInt = formuleInt(T, tirees)
                proba.append((100*probaInt / T ** (tirees)))
                xproba.append(i)
                tirees += 1


            # une fois le nombre de cartes tirees trouvees, on imprime le message
            print(str(5*i) + "%:\nCartes Tirees: " + str(tirees - 1) +
                  "\nPourcentage de Chances: " + str(100*probaInt / T ** (tirees-1)) + "%")
'''

main()
'''
plt.plot(X,Y, 'r',lw=2)
plt.title('Nombre de cartes nescessaires pour 99% en fonction du nombre total de cartes')
plt.xlabel('Nombre de cartes differentes')
plt.ylabel('Nombre de cartes tirees')
plt.legend()
plt.show()
'''