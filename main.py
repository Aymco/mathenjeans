import math
import matplotlib.pyplot as plt


proba= []
xproba= []

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
    for i in range( 5):
        T = (i+1) * _input

        tirées = 1
        probaInt = 0

        while 100 * probaInt <= 98 * T ** (tirées - 1):
            probaInt = formuleInt(T, tirées)
            proba.append((100 * probaInt / T ** (tirées)))
            xproba.append(i)
            tirées += 1

        print(str(T) + " : " + str(tirées-1))
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

