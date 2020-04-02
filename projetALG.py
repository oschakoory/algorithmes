#print("Etape 1: Aligner les séq 2 à 2 par Needleman et Wunsch")
#print("Etape 2: Matrix de distance")



#print("-------------------------------------------------------------------------------------------------")

print("Etape 3: Construire un arbre guide pour faire alignement multiple")
print("UPGMA")

from collections import defaultdict

lcluster=['A','B','C','D']
dist=defaultdict(lambda:defaultdict(float))
dist['A']['B']=0.4
dist['B']['A']=0.4
dist['A']['C']=0.2
dist['C']['A']=0.2
dist['A']['D']=0.9
dist['D']['A']=0.9
dist['B']['C']=0.4
dist['C']['B']=0.4
dist['B']['D']=0.85
dist['D']['B']=0.85
dist['C']['D']=0.9
dist['D']['C']=0.9

#Créer un cluster par seq
#tant que jai plusier cluster
	#Chercherles minimum
	#Clusteriser les minimum
	#Recalculer les distances

while len(lcluster) > 1:
	valmin= 1			#les distances sont < 1 alors min=1 ou >1 
	clustermin1= lcluster[0]	#initialiser le cluster au début avec AB
	clustermin2= lcluster[1]	#initialiser le cluster au début avec AB
	for c1 in lcluster:
		for c2 in lcluster:
			if c1 != c2 and dist[c1][c2] < valmin:
				valmin =  dist[c1][c2]
				clustermin1 = c1
				clustermin2 = c2
	#print(valmin)	
	lcluster.remove(clustermin1)
	lcluster.remove(clustermin2)
	newcluster='('+clustermin1+','+clustermin2+')'	#['AC', 'B', 'C']
	
	for clusterc in lcluster:
		dist[newcluster][clusterc] = dist[clusterc][clustermin1] + dist[clusterc][clustermin1]/2 #calculer dictance entre AC et B 
		dist[clusterc][newcluster] = dist[clusterc][clustermin2] + dist[clusterc][clustermin2]/2 #calculer dictance entre AC et D 
	lcluster.append(newcluster)
	#print(lcluster)
print(newcluster)
#(D,(B,(A,C)))


print("Neighbour Joining")


#print("------------------------------------------------------------------------------------------------------")

#print("Etape 4: Alignement multiple avec aide de arbre guide")
#print("Etape 5: Matrix de score")



#print("Etape 6: Construire un maximum parsimony tree")
