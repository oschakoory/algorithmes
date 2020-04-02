#Etape 3: Construire un arbre avec laide d'un matrix de score
print("Neighbour Joining")

from collections import defaultdict

dist = defaultdict(lambda: defaultdict(float))
distQ = defaultdict(lambda: defaultdict(float))
somcol = defaultdict(float)
newclusterNJ=[]

lclusterNJ=['A','B','C','D', 'E']
distNJ=defaultdict(lambda:defaultdict(float))
distNJ['A']['B']=5
distNJ['B']['A']=5
distNJ['A']['C']=9
distNJ['C']['A']=9
distNJ['A']['D']=9
distNJ['D']['A']=9
distNJ['A']['E']=8
distNJ['E']['A']=8
distNJ['B']['C']=10
distNJ['C']['B']=10
distNJ['B']['D']=10
distNJ['D']['B']=10
distNJ['B']['E']=9
distNJ['E']['B']=9
distNJ['C']['D']=8
distNJ['D']['C']=8
distNJ['C']['E']=7
distNJ['E']['C']=7
distNJ['D']['E']=3
distNJ['E']['D']=3

while len(lclusterNJ) > 1:
	
	valminNJ= 1000		
	clusterminNJ1= lclusterNJ[0]	
	clusterminNJ2= lclusterNJ[1]
	
	#Calculer la distance distQ
	for i in lclusterNJ:
		for j in lclusterNJ:
			somcol[i] += distNJ[i][j]
			distQ[i][j] = (len(lclusterNJ) - 2) * distNJ[i][j] - (somcol[i] + somcol[j])
			if i != j and distNJ[i][j] < valminNJ:
				valminNJ =  distNJ[i][j]
				clusterminNJ1 = i
				clusterminNJ2 = j
	 # modifier la liste de clusters, supprimer clusminNJ1 et clusminNJ2 de la liste de c
	lclusterNJ.remove(clusterminNJ1)
	lclusterNJ.remove(clusterminNJ2)

    # ajout des distances entre AC et ce qu'il y a dans les clusters
	newclusterNJ = ('(' + clusterminNJ1 + ',' + clusterminNJ2 + ')')

    # comparer à toute la liste de clusters
	for clusterC in lclusterNJ:
		distNJ[clusterC][newclusterNJ] = (distNJ[clusterC][clusterminNJ1] + distNJ[clusterC][clusterminNJ2]) / 2
		distNJ[newclusterNJ][clusterC] = (distNJ[clusterC][clusterminNJ1] + distNJ[clusterC][clusterminNJ2]) / 2
    # upgma prend une distance moyenne, ne permet pas d'estimer des dist
	lclusterNJ.append(newclusterNJ)
print(newclusterNJ)			
#((A,B),(C,(D,E)))


				
