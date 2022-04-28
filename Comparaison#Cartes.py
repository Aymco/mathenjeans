import libFormules as libF
import matplotlib.pyplot as plt

# liste des ordonnées
proba = []
# liste des abscisses
probaX = []


def main():

    maxCartes = int(input("#Types de cartes de 0 à: "))
    graphes = int(input("#Graphes différents: "))

    step = int(maxCartes / graphes)

    # on passe une fois pour chaque graphe
    for i in range(graphes):

        types = (i+1) * step
        tirées = 1
        probaInt = 0

        # on stocke toutes les valeurs dans le graphe jusqu'à 98%
        while 100 * probaInt <= 98 * types ** (tirées - 1):

            probaInt = libF.formuleInt(types, tirées)
            proba.append((100 * probaInt / types ** (tirées)))
            probaX.append(i)
            tirées += 1

        # on print toutes les valeurs dans le terminal
        # et on les met sur le graphe
        print(str(types) + " : " + str(tirées-1))
        plt.plot(proba, lw=2, label=str(types))

        # on réinitialise la liste pour le graphe suivant
        proba.clear()

    # on affiche le graphe
    plt.title('Probabilité pour ' + str(types) + ' cartes')
    plt.xlabel('Nombre de cartes tirées')
    plt.ylabel('Probabilitée')
    plt.legend()
    plt.show()


main()
