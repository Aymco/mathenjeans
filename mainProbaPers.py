import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

from mpl_toolkits.mplot3d import Axes3D

# la formule renvoie le resulat multiplié par types^tirées





proba = []
probaX = []

moy = []
moyX = []
esperances = []
ProbaTirees = []
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


    t = int(input("#Types de cartes : "))
    rept = int(input("#repetitions : "))
    Pers = int(input("#Personnes : "))
    #repP = int(input("#repetitions Personnes : "))

    Z = np.array([[0] * rept] * Pers)
    Ze = np.array([[0] * rept] * Pers)
    Zm = np.array([[0] * rept] * Pers)
    X = []
    Y = []
    for j in range(rept):
        T = t * (j + 1)
        X.append(T)
    for i in range(Pers):
        personnes = i + 1
        Y.append(personnes)

    for j in range(rept):
        for i in range(Pers):
            print("i" + str(i))
            print("j" + str(j))
            T =  t* (j+1)
            tirees = T
            personnes = i+1

            #print("nombres de personnes :")
            #print(personnes)

            probaInt = 0

            esperance = 0

            proba.append(0)
            probaX.append(0)
            proba.append(0)
            probaX.append(T - 1)

            while 100 * probaInt <= 99 :



                precProba = probaInt

                probaInt = formulePlusieurs(T, tirees, personnes)
                proba.append(probaInt * 100)
                probaX.append(tirees)

                # une fois le nombre de cartes tirees trouvées, on imprime le message
                # print(str(5*i) + "%:\nCartes tirees: " + str(tirees - 1) +
                #       "\nPourcentage de Chances: " + str(100*probaInt / T ** (tirees-1)) + "%")
                if(tirees%10 == 0):
                    print("\nPersonnes: " + str(personnes) + "\nTaille de la collection: " + str(
                        T) + "\nCartes tirees: " + str(tirees) + "\nProbabilitée de completer: " + str(
                        100 * probaInt) + "%")
                    #print("\nCartes tirees: " + str(tirees - 1) + "\nPourcentage de Chances: " + str(100*probaInt) + "%")
                    #print(tirees)
                #print(str(tirees)+" : "+str(probaInt * 100).replace(".", ","))


                probaInt
                p = (probaInt - precProba)
                #print(p)
                esperance += tirees * p
                moy.append(p)
                moyX.append(tirees)

                tirees += 1

            #print(str(T) + " cartes: Espérance: " + str(esperance))
            esperances.append(esperance)
            ProbaTirees.append(tirees)

            Zm[i,j] = T
            Z[i,j] = tirees
            Ze[i,j] = esperance

            plt.plot(moyX, moy, lw=2, label=str(T))
            moy.clear()
            moyX.clear()
            #plt.plot(probaX, proba, lw=1, label=str(personnes))
            #proba.clear()
            #probaX.clear()

    X, Y = np.meshgrid(X, Y)

    for i in range(Pers):
        print(str(T) + " cartes, " + str(i+1) + "Personnes : Espérance = " + str(esperances[i])+ " ; tirées = " + str(ProbaTirees[i]))

    #plt.title('Probabilité pour ' + str(T) + ' cartes avec 1 à 4 personnes')

    plt.legend()
    plt.grid(True)
    plt.show()

    print(Z)
    print(Ze)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(X, Y, Ze, color='r')
    #5 ax.plot_wireframe(X, Y, Zm, color='g')
    plt.show()
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(X, Y, Ze, color='r')
    ax.plot_wireframe(X, Y, Zm, color='g')
    plt.show()
main()