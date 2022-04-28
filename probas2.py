import libFormules as libF


def main():

    T = int(input("#Types de cartes : "))
    tirées = 1
    probaInt = 0

    for i in range(20):

        # on vérifie par échelle de 5% la probabilité
        while 20 * probaInt <= i * T ** (tirées - 1):

            probaInt = libF.formuleInt(T, tirées)
            tirées += 1

        # une fois le nombre de cartes tirées trouvées, on imprime le message
        print(str(5*i) + "%:\nCartes Tirées: " + str(tirées - 1) +
              "\nPourcentage de Chances: " + str(100*probaInt / T ** (tirées-1)) + "%")


if __name__ == "__main__":
    main()
