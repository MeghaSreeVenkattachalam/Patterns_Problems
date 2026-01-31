class solution:
    def printDescendingLetterTriangle(self, n):
        #Write your code here...
        for i in range(n,-1,-1):
            val = ord('A')
            for j in range(1,i+1):
                print(chr(val),end=" ")
                val+=1 
            print()


OUTPUT:

A B C D E F 
A B C D E 
A B C D 
A B C 
A B 
A 
