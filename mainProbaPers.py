import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

from mpl_toolkits.mplot3d import Axes3D

# la formule renvoie le resulat multiplié par types^tirées

X = [0,1,2,3]
Y = [2,2,1,3]
Z = [0,1,1,0]

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
plt.show()

proba = []
probaX = []
esperances = []
def formuleInt(types, tirees):
    somme = 0
    signe = 1
    for k in range(types):

        # la fonction choose s'appelle "comb" dans python
        somme += signe * math.comb(types, k) * (types - k) ** tirees

        # pour alterner + et - devant de maniere plus efficace que (-1)^k
        signe = -signe

    #print ("test: "  +" str(types ** tirees)+ "+ str(types)+" "+ str(tirees))
    return somme / types ** tirees


def formulePlusieurs(types, tirees, personnes):
    total = 1
    for n in range(personnes):
        total *= formuleInt(types, personnes * tirees - n * types)

    return total


def main():


    T = int(input("#Types de cartes : "))



    for i in range(1):

        tirees = 2 * T
        personnes = 1

        print("nombres de personnes :")
        print(personnes)

        probaInt = 0

        esperance = 0

        #proba.append(0)
        #probaX.append(0)
        #proba.append(0)
        #probaX.append(T - 1)

        while 100 * probaInt <= 99 :



            precProba = probaInt

            probaInt = formulePlusieurs(T, tirees, personnes)
            proba.append(probaInt * 100)
            probaX.append(personnes)

            # une fois le nombre de cartes tirees trouvées, on imprime le message
            # print(str(5*i) + "%:\nCartes tirees: " + str(tirees - 1) +
            #       "\nPourcentage de Chances: " + str(100*probaInt / T ** (tirees-1)) + "%")
            #if(tirees%100 == 0):
            print("\nPersonnes: " + str(personnes) + "\nTaille de la collection: " + str(T) +"\nCartes tirees: " + str(tirees) + "\nProbabilitée de completer: " + str(100*probaInt) + "%")
                #print(tirees)
            #print(str(tirees)+" : "+str(probaInt * 100).replace(".", ","))



            #p = (probaInt - precProba)
            #print(p)
            #esperance += tirees * p

            personnes += 1

        print(str(T) + " cartes: Espérance: " + str(esperance))
        #esperances[i] = esperance

        plt.plot(probaX, probaX, proba, lw=1, label=str(personnes))
        proba.clear()
        probaX.clear()

    #for i in range(3):
    #    print(str(T) + " cartes: Espérance: " + str(esperances[i]))

    #plt.title('Probabilité pour ' + str(T) + ' cartes avec 1 à 4 personnes')
    #plt.xlabel('Nombre de cartes tirées')
    #plt.ylabel('Probabilitée')
    plt.legend()
    plt.grid(True)
    plt.show()
main()