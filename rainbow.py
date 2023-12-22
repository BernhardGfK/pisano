import random

def noverk(n,k):
    q=1
    for i in range(k):
        q=q*(n-i)/(k-i)
    #print("noverk(",n,",",k,")=",q)
    return round(q)

# A function that calculates the number
# of possibilities for having chosen
# exactly k colors from a set of 
# n balls with k colors when choosing
# m balls.
def exactlyKColors(n,k,m):
    if m>n*k:
        return 0
    if m<k:
        return 0
    else:
        N=noverk(n*k,m)
        for i in range(1, k):
            N=N-noverk(k,i)*exactlyKColors(n,k-i,m)
        return N

#Function that calculates the probability
def prob(n,k,m):
    print("exactlyKColors("+str(n)+","+str(k)+","+str(m)+")=",exactlyKColors(n,k,m))
    print("porbability="+str(exactlyKColors(n,k,m)/noverk(n*k,m)))

#for k in range(2,8):
#    prob(k,k,k)
#    print("")
prob(10,7,20)
#exit(0)

N=100000
ac=0
for n in range(N):
    q=0
    sam=random.sample(range(0,69), 20)
    for c in range(7):
        cf=False
        for i in sam:
            if i>=c*10 and i<(c+1)*10:
                cf=True
                #print("color ",c," is in the sample")
                break
        if cf==True:
            q+=1
    if q==7:
        #print(str(n)+". all colors are in the sample")
        ac+=1
print("probability of all colors in the sample: ",ac/N)

q=1
for i in range(20):
    q=q*(60-i)/(70-i)
print("probabilitt that a given color is present: ",1-q)
print("probability of all colors in the sample (if this were independent): ",(1-q)**7)
