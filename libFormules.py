import math

def formuleRapide(listC, T):
    for i in range(T):
        value = listC[T-i-1]
        if(i!=0):
            #transition diagonale
            listC[T-i] += value * (i+1)

        #transition verticale
        listC[T-i-1] = value * (T-i-0)
            
    return (listC)


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


# la formule renvoie le resulat réel
def formuleFloat(types, tirees):
    somme = 0
    signe = 1
    for k in range(types):

        # la fonction choose s'appelle "comb" dans python
        somme += signe * math.comb(types, k) * (types - k) ** tirees

        # pour alterner + et - devant de maniere plus efficace que (-1)^k
        signe = -signe

    #print ("test: "  +" str(types ** tirees)+ "+ str(types)+" "+ str(tirees))
    return somme / types ** tirees


def formulePlusieurs(types, tirees, personnes):
    total = 1
    for n in range(personnes):
        total *= formuleFloat(types, personnes * tirees - n * types)

    return total