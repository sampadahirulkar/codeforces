# failed test 22
# do not use
'''You've got a 5 × 5 matrix, consisting of 24 zeroes and a single number one. Let's index the matrix rows by numbers from 1 to 5 from top to bottom, let's index the matrix columns by numbers from 1 to 5 from left to right. In one move, you are allowed to apply one of the two following transformations to the matrix:

Swap two neighboring matrix rows, that is, rows with indexes i and i + 1 for some integer i (1 ≤ i < 5).
Swap two neighboring matrix columns, that is, columns with indexes j and j + 1 for some integer j (1 ≤ j < 5).
You think that a matrix looks beautiful, if the single number one of the matrix is located in its middle (in the cell that is on the intersection of the third row and the third column). Count the minimum number of moves needed to make the matrix beautiful.

Input
The input consists of five lines, each line contains five integers: the j-th integer in the i-th line of the input represents the element of the matrix that is located on the intersection of the i-th row and the j-th column. It is guaranteed that the matrix consists of 24 zeroes and a single number one.

Output
Print a single integer — the minimum number of moves needed to make the matrix beautiful.'''




r1 = list(map(int,input().split()))
r2 = list(map(int,input().split()))
r3 = list(map(int,input().split()))
r4 = list(map(int,input().split()))
r5 = list(map(int,input().split()))
if r1[0]+r1[4]+r5[1]+r5[4]!=0:
    print(4)
elif r1[1]+r1[3]+r2[0]+r2[4]+r4[0]+r4[4]+r5[1]+r5[3]!=0:
    print(3)
elif r2[2]+r3[1]+r3[3]+r4[2]!=0:
    print(1)
elif r3[2]!=0:
    print(0)
else:
    print(2)