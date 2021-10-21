def countCouple(inline):
  inline = input().lower()
  pairs = set()
  for i in range(0,len(inline)):
	  if inline[i:i+2].isalpha() and len(inline[i:i+2]) == 2:
		    pairs.add(inline[i:i+2])
  return len(pairs)
countCouple (input())
