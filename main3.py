import libFormules as libF
import matplotlib.pyplot as plt

proba = []
probaX = []
X= []
Y = []


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

            listCalcul = libF.formuleRapide(listCalcul, T)
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


main()

plt.plot(X,Y, 'r',lw=2)
plt.title('Nombre de cartes nescessaires pour 99% en fonction du nombre total de cartes')
plt.xlabel('Nombre de cartes differentes')
plt.ylabel('Nombre de cartes tirees')
plt.legend()
plt.show()
''''''