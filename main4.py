import libFormules as libF
import matplotlib.pyplot as plt
# la formule renvoie le resulat multiplié par types^tirées

proba = []
probaX = []
esperances = []


def main():


    T = int(input("#Types de cartes : "))



    for i in range(3):

        tirees = T
        personnes = 2

        print("nombres de personnes :")
        print(personnes)

        probaInt = 0

        esperance = 0

        proba.append(0)
        probaX.append(0)
        proba.append(0)
        probaX.append(T - 1)

        while 100 * probaInt <= 99 :



            precProba = probaInt

            probaInt = libF.formulePlusieurs(T, tirees, personnes)
            proba.append(probaInt * 100)
            probaX.append(tirees)

            # une fois le nombre de cartes tirees trouvées, on imprime le message
            # print(str(5*i) + "%:\nCartes tirees: " + str(tirees - 1) +
            #       "\nPourcentage de Chances: " + str(100*probaInt / T ** (tirees-1)) + "%")
            if(tirees%100 == 0):
                print("\nCartes tirees: " + str(tirees - 1) + "\nPourcentage de Chances: " + str(100*probaInt) + "%")
                #print(tirees)
            #print(str(tirees)+" : "+str(probaInt * 100).replace(".", ","))


            probaInt
            p = (probaInt - precProba)
            #print(p)
            esperance += tirees * p

            tirees += 10

        print(str(T) + " cartes: Espérance: " + str(esperance))
        esperances.append(esperance)

        plt.plot(probaX, proba, lw=1, label=str(personnes))
        proba.clear()
        probaX.clear()

    for i in range(3):
        print(str(T) + " cartes: Espérance: " + str(esperances[i]))

    #plt.title('Probabilité pour ' + str(T) + ' cartes avec 1 à 4 personnes')
    #plt.xlabel('Nombre de cartes tirées')
    #plt.ylabel('Probabilitée')
    plt.legend()
    plt.grid(True)
    plt.show()
main()