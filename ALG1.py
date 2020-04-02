T=[5,4,9,8,1,6]

def partition(H,d,f,p):	
	j=d + 1
	for i in range (d+1, f+1):
		if H[i]< H[p]:
			a=H[i]
			H[i]=H[j]
			H[j]=a
			j+=1
	a=H[d]
	H[d]=H[j-1]
	H[j-1]=a
	return j-1

def tri(deb,fin):
	if fin>deb:
		ipivot=deb  #ipivot=choixPivot(deb,fin)
		ipivot2=partition(deb,fin,ipivot)
		tri(deb, ipivot2 - 1)
		tri(ipivot2 + 1, fin) 

tri(0,len(T)-1)
print(T)
			


	
