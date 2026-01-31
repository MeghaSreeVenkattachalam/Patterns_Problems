class solution:
    def printCenteredStarTriangle(self, n):
        #Write your code here...
        for i in range(n):
            print(" "*(n-i-1)+"*"*((i+1)*2-1))
OUTPUT:

  *
 ***
*****
