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
            listCalcul = libF.formuleBrute(listCalcul, T)
            proba = listCalcul[T - 1] / T ** (tirees)
            p = (proba - precProba)
            print(p)
            esperance += tirees * p

            tirees += 1


        print(str(T) + " cartes: Espérance: " + str(esperance))
        

main()