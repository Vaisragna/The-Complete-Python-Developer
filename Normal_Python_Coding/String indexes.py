##[String indexes]##

'me me me' #stored in order on the computer
#01234567  locations(indexes)
#one can access part of a string regarding the indexes

selfish = 'me me me'
print(selfish[0])
print(selfish[7])
print(selfish)

selfish = '01234567'
        #  01234567
#[start:stop]        
print(selfish[0:2])
print(selfish[0:7])
print(selfish[0:8])
#[start:stop:stepover]
print(selfish[0:8:1])
print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[::1])
# reverse
print(selfish[-1])
print(selfish[-2])
print(selfish[-3])
print(selfish[::-1])
print(selfish[::-2])