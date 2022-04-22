import math

# la formule renvoie le resulat multiplié par types^tirées
def formuleInt(types, tirées):
    somme = 0
    signe = 1
    for k in range(types):

        # la fonction choose s'appelle "comb" dans python
        somme += signe * math.comb(types, k) * (types - k) ** tirées

        # pour alterner + et - devant de maniere plus efficace que (-1)^k
        signe = -signe

    return somme


def main():

    T = int(input("#Types de cartes : "))
    tirées = 1
    probaInt = 0

    for i in range(20):

        # on vérifie par échelle de 5% la probabilité
        while 20 * probaInt <= i * T ** (tirées - 1):

            probaInt = formuleInt(T, tirées)
            tirées += 1

        # une fois le nombre de cartes tirées trouvées, on imprime le message
        print(str(5*i) + "%:\nCartes Tirées: " + str(tirées - 1) +
              "\nPourcentage de Chances: " + str(100*probaInt / T ** (tirées-1)) + "%")


if __name__ == "__main__":
    main()
