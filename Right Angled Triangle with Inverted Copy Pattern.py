class solution:
    def printTrianglePattern(self, n):
        #Write your code here...
        for i in range(n):
            print("* "*(i+1))
        for i in range(n-1,-1,-1):
            print("* "*(i))

OUTPUT:

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


