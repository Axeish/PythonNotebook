'''
recursion; 
when a fucntion call itself directly or indirectly

a base case is a condition that  that will break the self calling loop


'''

#----------------------------------
def factorial(n):
  '''
  factorial using recusrion
  '''  
  if  n <= 1 : #base factor
    return n
  else :
    return n* factorial(n-1)	


print(factorial(7))         

#-----------------------------

delivery = 1

print ("%d is responsibel"%deli)
def delivery(gift):
    global deli 	
    print ("%d is responsibel"%deli)
    if len(gift) == 1 :
        print ("del %s delivered by %s"%(gift[0],deli))


    else:
       
       mid = len(gift)//2 
       first = gift[mid:] 
       last = gift[:mid]
       deli = deli+1  
       delivery(first)
       deli = deli+1
       delivery(last)

print(delivery(["hema","jaya","rekha","sushma"]))
