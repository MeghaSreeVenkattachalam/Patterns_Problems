class solution:
    def printLetterTriangle(self, n):
        # Write your code here...
        for i in range(1,n+1):
            val = ord('A')
            for j in range(1,i+1):
                print(chr(val),end=" ")
                val+=1
            print()


OUTPUT:

A 
A B 
