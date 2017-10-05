def RowFromBottom(B,k):
 n=len(B)
 return B[n-k-1]

def lg(n):
 x=0
 while (2**x)<=n:
        x+=1
 return x-1

def CreateZeroArray(n,m):
 C=[0]*m
 W=[0]*n
 for i in range(0,n):
  W[i]=C
 return W

def Num(A):
 s=0
 n=len(A)
 i=n-1
 for x in A:
  s=s+x*(2**i)
  i=i-1
 return s  

def dualsum(a,b):
    if (a==0) & (b==0):
	    s=0
    else:
	     s=1
    return s	

def listsum(u,v):
    w=[]
    for i in range (0,len(u)):
     w.append(dualsum(u[i],v[i]))
    return w


def splitB(B):
    n=len(B)
    m=lg(n)
    s=int(n/m)+1
    C=[]
    for j in range(0,n,s,):
     C.append(B[j:j+s])
     
    return C

def split(A):
    n=len(A)
    m=lg(n)
    s=int(n/m)+1
    C=[[]]*n
    for i in range(0,n):
     for j in range(0,n,s,):
         C[i].append(A[i][j:j+s])

    return C
        

        

def FourRussians(array1,array2,n):
    f = open( "array1.txt" )

    A = []
    for line in f.readlines():
     y = [value for value in line.split()]
     A.append( y )


    f = open( "array2.txt" )

    B = []
    for line in f.readlines():
     y = [value for value in line.split()]
     B.append( y )
    


    A=splitA(A)
    B=splitB(B)


    
    m=lg(n)
    C=CreateZeroArray(n,n)
    for i in range (1,int(n/m)+2):
      rs=CreateZeroArray(2**m,n)
      rs[0]=[0]*n
      bp=1
      k=0  
      for j in range(1,2**m +1):
          rs[j]=listsum(rs[j-2**k],RowFromBottom(B[i],k+1))
          if (bp==1) :
              bp=j+1
              k=k+1
          else:
              bp=bp-1
      C[i]=CreateZeroArray(n,n)
      for j in range(0,n+1):
          C[i][j]=rs[Num(A[i][j])]
      for z in range(0,n+1):
          C[z]=listsum(C[z],C[i][z])
      return C    
