arr = ['lint', 'code', 'for', 'life']
#Encoding
res = ''
for i in arr:
    res += str(len(i)) + '#' + i 

#Decoding
decres, i = [], 0
while i < len(res):
    j = i
    while res[j] != '#':
        j += 1
    length = int(res[i:j])
    decres.append(res[j+1: j+1+length])
    i = j+1+length

print(res)
print(decres)
