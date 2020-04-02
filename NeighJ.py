# algorithme agglomeratif, plus grouton que upgma
# alignement 2 a 2 -> matrice distances
# tant que l'on n'a pas tout clusterisé
# calcul de la matrice de distance Q
# recherche de la distance Q min (-> entre A et B)
# calcul de la distance entre le nouveau noeud ancetre U et le couple de départ avec Q min AB
# d(A,U)=1/2d(A,B) + 1/(2*(n-2)) * (somme pour k de 1 a n de d(A,k) - somme pour k de 1 a n de d(B,k))
# d(A,U)=2, d(B,U)=3
# supression des noeuds A et B
# calcul des distances entre le nouveau noeud/sommet U et les noeuds restants
# d(U,C) = 1/2 ( d(A,C) + d(B,C) - d(A,B) ) = 7
# d(U,D) = 7
# d(U,E) = 6

from collections import defaultdict

# soit 5 noeuds, 5 sequences

dist = defaultdict(lambda: defaultdict(float))
distQ = defaultdict(lambda: defaultdict(float))
somcol = defaultdict(float)

lcluster = ['A', 'B', 'C', 'D', 'E']
dist['A']['B'] = 5
dist['B']['A'] = 5
dist['A']['C'] = 9
dist['C']['A'] = 9
dist['A']['D'] = 9
dist['D']['A'] = 9
dist['A']['E'] = 8
dist['E']['A'] = 8
dist['B']['C'] = 10
dist['C']['B'] = 10
dist['B']['D'] = 10
dist['D']['B'] = 10
dist['B']['E'] = 9
dist['E']['B'] = 9
dist['C']['D'] = 8
dist['D']['C'] = 8
dist['C']['E'] = 7
dist['E']['C'] = 7
dist['D']['E'] = 3
dist['E']['D'] = 3

# dist la plus courte est entre D et E, puis 2ieme + courte: AB
# distDE-A: 8.5, distDE-B: 9.5, distDE-C:7.5
# distAB-C: 9.5

# neighbor joining regroupe d'abord les seq les plus proches entre elles et les plus distantes du reste, calcule le noeud 'ancetre commun' des seq les + proches, puis regroupe les branches d'arbre avec les noeuds/seq plus lointains en utilisant les noeuds 'ancetre commun' précédemment calculés.

# Coeff Q(A,B) = (n-2)d(A,B) - somme de k allant de 1 à n de d(A,k) - somme de k allant de 1 à n de d(B,k)

# les seq AB sont a la fois les + proches et + eloignees des autres
# Calcul de la distance entre noeud AB tenant compte de la distancede A et de B avec les autres points:
# Q(A,B)= 3*5 - (9+9+8+5 + 10+10+9+5) = -50
# Q(A,C)= 3*9 - (5+9+8+9 + 10+8+7+9) = -38

# Calcul de la matrice Q:
'''
distQ['A']['B']=-50
distQ['B']['A']=-50
distQ['A']['C']=-38
distQ['C']['A']=-38
distQ['A']['D']=-34
distQ['D']['A']=-34
distQ['A']['E']=-34
distQ['E']['A']=-34
distQ['B']['C']=-38
distQ['C']['B']=-38
distQ['B']['D']=-34
distQ['D']['B']=-34
distQ['B']['E']=-34
distQ['E']['B']=-34
distQ['C']['D']=-40
distQ['D']['C']=-40
distQ['C']['E']=-40
distQ['E']['C']=-40
distQ['D']['E']=-48
distQ['E']['D']=-48
'''

# On boucle sur les clusters tant qu'il y a plusieurs clusters
while len(lcluster) > 1:
    print('-----------------------------------------------------------------')
    print(lcluster)
    mini = 1000  # On part haut pour enregistrer les minimums successifs
    noeudmini1 = lcluster[0]
    noeudmini2 = lcluster[1]

    # calcul matrice Q
    for c1 in lcluster:
        for c2 in lcluster:
            somcol[c1] += dist[c1][c2]

        for c2 in lcluster:
            distQ[c1][c2] = (len(lcluster) - 2) * dist[c1][c2] - (somcol[c1] + somcol[c2])
        # print(c1,c2)

    # Chercher le minimum pour toute la matrice
    for c1 in lcluster:
        for c2 in lcluster:
            if c1 != c2 and dist[c1][c2] < mini:
                mini = dist[c1][c2]
                clusmin1 = c1
                clusmin2 = c2
            # print(mini)

    # modifier la liste de clusters, supprimer clusmin1 et clusmin2 de la liste de c
    lcluster.remove(clusmin1)
    lcluster.remove(clusmin2)

    # ajout des distances entre AC et ce qu'il y a dans les clusters
    newcluster = ('(' + clusmin1 + ',' + clusmin2 + ')')

    # comparer à toute la liste de clusters
    for cc in lcluster:
        dist[cc][newcluster] = (dist[cc][clusmin1] + dist[cc][clusmin2]) / 2
        dist[newcluster][cc] = (dist[cc][clusmin1] + dist[cc][clusmin2]) / 2
    # upgma prend une distance moyenne, ne permet pas d'estimer des dist
    # differentes entre chacun des 2 points d'une fourche et le noeud en amont.
    lcluster.append(newcluster)
