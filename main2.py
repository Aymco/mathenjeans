import libFormules as libF
import matplotlib.pyplot as plt

proba = []
X= []
Y = []


def main():
    _input = int(input("#Types de cartes : "))
    for i in range(7):
        T = (i + 1) * _input

        tirées = 1
        probaInt = 0

        while 100 * probaInt <= 98 * T ** (tirées - 1):
            probaInt = libF.formuleInt(T, tirées)
            proba.append((100 * probaInt / T ** (tirées)))

            tirées += 1

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


main()
plt.plot(X,Y,lw=2)
plt.title('Nombre de cartes nescessaires pour 98% en fonction du nombre total de cartes')
plt.xlabel('Nombre de cartes différentes')
plt.ylabel('Nombre de cartes tirées')
plt.legend()
plt.show()