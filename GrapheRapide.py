import libFormules as libF
import matplotlib.pyplot as plt

# liste des ordonnées
proba = []
# liste des abscisses
probaX = []


def main():
    types = int(input("#Types de cartes : "))

    # on initialise une liste de longueur types pour la
    # méthode de calcul rapide
    listCalcul = [0] * types
    listCalcul[0] = 1

    tirees = 1
    probaInt = 0

    # on cherche les valeurs du graphe jusqu'à 99%
    while 100 * probaInt <= 99 * types ** (tirees - 1):

        probaInt = listCalcul[types - 1]
        p = (100 * probaInt / types ** (tirees))

        # tous les 50 tirages, on print la probabilité
        if(tirees % 50 == 0):
            print(str(tirees) + ": " + str(p).replace(".", ","))

        # on ajoute les valeurs au graphe
        proba.append(p)
        probaX.append(tirees)

        # on update la liste et on incrémente tirées
        listCalcul = libF.formuleRapide(listCalcul, types)
        tirees += 1

    # on affiche le graphe et on print le minimum pour 99%
    print(str(tirees) + " : " + str(p))
    plt.plot(probaX, proba,  lw=2, label=str(types))
    plt.plot(types, 0, 'bo', lw=3)

    plt.title('Probabilité pour ' + str(types) + ' cartes')
    plt.xlabel('Nombre de cartes tirées')
    plt.ylabel('Probabilité')
    plt.legend()
    plt.grid(True)
    plt.show()


main()
