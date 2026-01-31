class solution:
    def printAlternatingBinaryTriangle(self, n):
        #Write your code here...

        for i in range(1,n+1):
            for j in range(1,i+1):
               if (i+j)%2==0:
                   print(1,end=" ")
               else:
                   print(0,end=" ")
            print()


OUTPUT:

1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
0 1 0 1 0 1 
