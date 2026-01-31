class solution:
    def printCombinedTriangle(self, n):
        #Write your code here...
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end=" ")
            print(" "*((n-i)*4),end="")
            for j in range(i,0,-1):
                print(j,end=" ")
            print()


OUTPUT:

1             1 
1 2         2 1 
1 2 3     3 2 1 
1 2 3 4 4 3 2 1 
