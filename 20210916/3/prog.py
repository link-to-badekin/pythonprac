numl = eval(input())
mxnum = numl[0]
for num in numl[1:]:
	mxnum = num if num > mxnum else mxnum 
print(mxnum)
