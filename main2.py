import math
import matplotlib.pyplot as plt

proba = []
X= []
Y = []
print("ok")


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
    _input = int(input("#Types de cartes : "))
    step = int(input("#ecart : "))
    for i in range(1):
        T = (i + 1) * _input

        tirées = T * 5
        probaInt = 0

        while 100 * probaInt <= 98 * T ** (tirées - step):
            probaInt = formuleInt(T, tirées)
            proba.append((100 * probaInt / T ** (tirées)))
            print("\nPersonnes: " + str(1) + "\nTaille de la collection: " + str(T) + "\nCartes tirees: " + str(tirées) + "\nProbabilitée de completer: " + str(100 * probaInt) + "%")

            tirées += step

        print(str(T) + " : " + str(tirées - 1))
        X.append(T)
        Y.append(tirées - 1)
        plt.plot(proba, lw=2, label=str(T))
        proba.clear()
    print(proba)

    plt.title('Probabilité pour ' + str(T) + ' cartes')
    plt.xlabel('Nombre de cartes tirées')
    plt.ylabel('Probabilitée')
    plt.legend()
    plt.show()


'''
        for i in range(20):

            # on vérifie par échelle de 5% la probabilité
            while 20 * probaInt <= i * T ** (tirées - 1):


                probaInt = formuleInt(T, tirées)
                proba.append((100*probaInt / T ** (tirées)))
                xproba.append(i)
                tirées += 1


            # une fois le nombre de cartes tirées trouvées, on imprime le message
            print(str(5*i) + "%:\nCartes Tirées: " + str(tirées - 1) +
                  "\nPourcentage de Chances: " + str(100*probaInt / T ** (tirées-1)) + "%")
'''

main()
plt.plot(X,Y,lw=2)
plt.title('Nombre de cartes nescessaires pour 98% en fonction du nombre total de cartes')
plt.xlabel('Nombre de cartes différentes')
plt.ylabel('Nombre de cartes tirées')
plt.legend()
plt.show()