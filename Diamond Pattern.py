class solution:
    def printDoubleCenteredStarTriangle(self, n):
        #Write your code here...
        for i in range(n):
            print(" "*(n-i-1)+"*"*((i+1)*2-1))
        for i in range(n,-1,-1):
            print(" "*(n-i)+"*"*(i*2-1))

OUTPUT:

  *
 ***
*****
*****
 ***
  *
