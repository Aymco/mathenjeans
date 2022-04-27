import math
import matplotlib.pyplot as plt

proba = []
probaX = []
X= []
Y = []
print("ok")



'''
# la formule renvoie le resulat multiplie par types^tirees
def formuleInt(types, tirees):
    somme = 0
    signe = 1
    for k in range(types):
        # la fonction choose s'appelle "comb" dans python
        somme += signe * math.comb(types, k) * (types - k) ** tirees

        # pour alterner + et - devant de maniere plus efficace que (-1)^k
        signe = -signe

    return somme
'''

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
        plt.plot(T-1, 0, 'bo', lw=3)
        listCalcul[0] = 1
        print(listCalcul)
        tirees = 2
        probaInt = 0

        proba.append(0)
        probaX.append(0)
        proba.append(0)
        probaX.append(1)

        
        


        while 100 * probaInt <= 99 * T ** (tirees - 1):

            listCalcul = formuleBrute(listCalcul, T)
            #print(listCalcul)
            probaInt = listCalcul[T - 1]
            p = (100 * probaInt / T ** (tirees))
            if(tirees%100 == 0):
                print("\nPersonnes: " + str(1) + "\nTaille de la collection: " + str(
                    T) + "\nCartes tirees: " + str(tirees) + "\nProbabilitée de completer: " + str(
                    100 * probaInt) + "%")

                #print( str(tirees)+  "  " +  str(p).replace(".", ","))
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

    plt.title('Probabilitée pour ' + str(T) + ' cartes')
    plt.xlabel('Nombre de cartes tirées')
    plt.ylabel('Probabilitée')
    plt.legend()
    plt.grid(True)
    plt.show()


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

plt.plot(X,Y, 'r',lw=2)
plt.title('Nombre de cartes nescessaires pour 99% en fonction du nombre total de cartes')
plt.xlabel('Nombre de cartes differentes')
plt.ylabel('Nombre de cartes tirees')
plt.legend()
plt.show()
''''''