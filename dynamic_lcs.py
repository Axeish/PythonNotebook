


def lcs(x,y,m,n):
'''
  Least common subsequence
'''
  if m==0 or n==0 :
    return 0
  elif x[m-1] == y[n-1]:
    return 1+ lcs(x,y,m-1,n-1)
  else:
    return max(lcs(x,y,m-1,n), lcs(x,y,m,n-1)) 

 


def scs(x,y,m,n):
'''
  Short common supersequence
'''	
  if m==0 or n==0 :
    return m+n
  elif x[m-1] == y[n-1]:
    val = 1+ scs(x,y,m-1,n-1)
    print (val)
    return val
  else:
    val = min(scs(x,y,m-1,n)+1, scs(x,y,m,n-1)+1) 
    print (val)
    return val
 



x= "daol"
y= "pola"


print(scs(x,y, len(x), len(y)))    