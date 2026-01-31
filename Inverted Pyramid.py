class solution:
    def printInvertedCenteredStarTriangle(self, n):
        #Write your code here...
        
        for i in range(n,-1,-1):
            print(" "*(n-i)+"*"*(i*2-1))


OUTPUT:

*****
 ***
  *
