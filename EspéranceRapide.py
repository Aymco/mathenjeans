import types
import libFormules as libF

def main():

    types = int(input("#Types de cartes : "))
    
    # on initialise une liste de longueur types pour la
    # méthode de calcul rapide
    listCalcul = [0] * types
    listCalcul[0] = 1

    tirees = 1
    esperance = 0
    proba = 0

    # on calcule l'espérance jusqu'à 99%
    while 100 * proba <= 99:

        # on garde la valeur précédente en mémoire
        precProba = proba

        # on update la probabilité
        proba = listCalcul[-1] / types ** (tirees)

        # on calcule la différence entre la proba actuelle et précédente
        # et on en fait la somme pour calculer l'espérance
        p = (proba - precProba)
        esperance += tirees * p

        # on update la liste
        listCalcul = libF.formuleRapide(listCalcul, types)
        # on incrémente tirées
        tirees += 1

    # on print le résultat
    print(str(types) + " cartes: Espérance: " + str(esperance))
        

main()