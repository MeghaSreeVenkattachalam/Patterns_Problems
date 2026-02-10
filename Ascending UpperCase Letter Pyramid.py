class solution:
    def printAscLetterPyramid(self, n):
        #Write your code here...
        for i in range(1,n+1):
            start = chr(65+n-i)
            for j in range(i):
                print(chr(ord(start)+j),end=" ")
            print()


OUTPUT:


F 
E F 
D E F 
C D E F 
B C D E F 
A B C D E F
