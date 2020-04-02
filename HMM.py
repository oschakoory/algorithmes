
print("HMM Algorithm Viterbi")

from collections import defaultdict

v = defaultdict(lambda: defaultdict(float))
score = defaultdict(lambda: defaultdict(float))
etat_prec = defaultdict(lambda: defaultdict(float))
maxscore = defaultdict(lambda: defaultdict(float))

sym=['dormir','dormir','dormir','courir','manger'] #une suite de symbol connu 
states={'normal','hyper'} #on a deux états 

prob_emit={'normal':{'dormir':0.8,'manger':0.02,'courir':0.18},'hyper':{'dormir':0.5,'manger':0.02,'courir':0.48}} #les probabilités demission dans un dico 2D

prob_trans={'normal':{'normal':0.9,'hyper':0.1},'hyper':{'normal':0.5,'hyper':0.5}} #les probabilités de transition dans un dico 2D

prob_start={'normal':0.9,'hyper':0.1} #les starts probabilités dans un dico 1D

#initialiser le 1er étape en utilisant le prob_start
v[0]['normal']={'score':0.9,'etat_prec':'s'}
score[0]['normal']=0.9
etat_prec[0]['normal']='dormir'


for e in states:
	score[0][e]=prob_start[e]
	etat_prec[0][e]= None

#Pour chaque obs i (manger, courir, dormir)
for i in range(1,len(sym)):
	#Pour chaque état e (normal, hyper)
	for E in states:
		maxscore[i][E]=0
		#Pour chaque état précedent p
		for p in states:
			new_score = score[i-1][p] * prob_emit[p][sym[i-1]] * prob_trans[p][E]
			if new_score > maxscore[i][E]:
				maxscore[i][E]=new_score
				etat_prec[i][E]=p
print(etat_prec)








