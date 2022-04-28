import libFormules as libF
import matplotlib.pyplot as plt

X = []
Y = []


def main():

    maxCartes = int(input("#Types de cartes de 0 à: "))
    valeurs = int(input("#Valeurs: "))

    step = int(maxCartes / valeurs)

    # on passe une fois pour chaque valeur
    for i in range(valeurs):

        types = (i+1) * step

        tirées = 1
        probaInt = 0

        # on cherche le nombre minimum de cartes tirées pour 98% de chances
        while 100 * probaInt <= 98 * types ** (tirées - 1):

            probaInt = libF.formuleInt(types, tirées)
            tirées += 1

        # on print les valeurs trouvées et les ajoute au graphe
        print(str(types) + " : " + str(tirées - 1))
        X.append(types)
        Y.append(tirées - 1)

    # onj affiche le graphe
    plt.plot(X, Y, lw=2)
    plt.title(
        'Nombre de cartes nescessaires pour 98% en fonction du nombre de types')
    plt.xlabel('Nombre de cartes différentes')
    plt.ylabel('Nombre de cartes tirées')
    plt.legend()
    plt.show()


main()
