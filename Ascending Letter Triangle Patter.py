class solution:
    def printAscLetterTriangle(self, n):
        #Write your code here...
        val = ord('A')
        for i in range(1,n+1):
            print((chr(val)+" ")*i)
            val+=1

OUTPUT:

A 
B B 
C C C 
D D D D 
E E E E E 
