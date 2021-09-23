"""
A: четные, делящиеся на 25
B: нечетные, делящиеся на 25
C: делящиеся на 8
"""
A,B,C = [],[],[]
data = int( input() )
if (data%25==0):
     print( "A+ B-" if data%2==0 else "A- B+", end = " ")
else: print("A- B-", end = " ")
print ("C+"  if (data%8 == 0) else "C-")



