def mSort( l,r ):
  if len(l) > 1 :
    l = mSort( l[:len(l)//2],l[len(l)//2:] )
  if len(r) > 1 :
    r = mSort( r[:len(r)//2],r[len(r)//2:] )
  retArray = []
  print("l =",l,"r =",r)
  while len(r) > 0 or len(l) > 0:
    if len(l) <= 0:
      retArray.append(r.pop(0))
      continue
    if len(r) <= 0:
      retArray.append(l.pop(0))
      continue
    if l[0] < r[0]:
      retArray.append(l.pop(0))
    else:
      retArray.append(r.pop(0))
  return retArray

testArray = [1,5,2,5,7,8,9,6,3]
print(mSort(testArray[:len(testArray)//2],testArray[len(testArray)//2:]))
print(sorted(testArray))
