class solution:
    def printTriangleInverted(self, n):
        # Write your code here...
        for i in range(n,-1,-1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()


OUTPUT:

1 2 
1 
