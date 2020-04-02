#Etape 3: Construire un arbre avec laide d'un matrix de score
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
	for i in lcluster:
		for j in lcluster:
			if i != j and dist[i][j] < valmin:
				valmin =  dist[i][j]
				clustermin1 = i
				clustermin2 = j	
	#print(valmin)	
	lcluster.remove(clustermin1)
	lcluster.remove(clustermin2)
	newcluster='('+clustermin1+','+clustermin2+')'	#['AC', 'B', 'C']
	
	for clusterc in lcluster:
#calculer dictance entre AC et B 
		dist[newcluster][clusterc] = dist[clusterc][clustermin1] + dist[clusterc][clustermin2]/2 
#calculer dictance entre CA et B
		dist[clusterc][newcluster] = dist[clusterc][clustermin1] + dist[clusterc][clustermin2]/2 
	lcluster.append(newcluster)
	#print(lcluster)
print(newcluster)
#(D,(B,(A,C)))

				
			
			


	
		
		
		
