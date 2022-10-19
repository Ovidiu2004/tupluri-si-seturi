X={1,2,3,4,5,6,7,111,112,113,114} 
Y={1,2,3,44,45,46,47,199}
print('X|Y *reuniunea=', X|Y )
print('X&Y *intersectia=', X&Y )
print('X\Y *raportul=', X-Y)
print('(X\Y)|(Y\X)  *reuniunea raporturilor=',(X-Y)|(Y|X))
print('(X\Y)ꓵ(Y\X)  *intersectia raporturilor=',(X-Y)&(Y|X))