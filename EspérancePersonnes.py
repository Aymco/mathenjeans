import types
import libFormules as libF
import matplotlib.pyplot as plt
# la formule renvoie le resulat multiplié par types^tirées

proba = []
probaX = []
esperances = []


def main():

    T = int(input("#Types de cartes : "))
    maxPers = int(input("#Maximum personnes: "))

    # on fait une boucle pour chaque nombre de personnes
    for i in range(maxPers):

        # puisque la probabilité en-dessous de T est 0, on commence en T
        tirees = T
        personnes = 1 + i

        probaInt = 0
        esperance = 0

        # on calcule l'espérance et on stocke les valeurs jusqu'à 99%
        while 100 * probaInt <= 99:

            # on garde la valeur précédente en mémoire
            precProba = probaInt

            # on ajoute les valeurs au graphe
            proba.append(probaInt * 100)
            probaX.append(tirees)

            # on update la probabilité
            probaInt = libF.formulePlusieurs(T, tirees, personnes)

            # on calcule la différence entre la proba actuelle et précédente
            # et on en fait la somme pour calculer l'espérance
            p = (probaInt - precProba)
            esperance += tirees * p

            # on incrémente le nombre de cartes tirées
            tirees += 10

        # on print les valeurs trouvées et on vide les listes
        # pour le prochain passage
        print(str(personnes) + " personnes: Espérance: " + str(esperance))
        esperances.append(esperance)

        plt.plot(probaX, proba, lw=1, label=str(personnes))
        proba.clear()
        probaX.clear()

    # on affiche le graphe final
    plt.title('Probabilité pour ' + str(T) +
              ' cartes avec 1 à ' + str(maxPers) + ' personnes')
    plt.xlabel('Nombre de cartes tirées')
    plt.ylabel('Probabilité')
    plt.legend()
    plt.grid(True)
    plt.show()


main()
