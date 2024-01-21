import sys

# comment증가
comment = 0
for i in range(10):
    comment += 1
    
    
def funcion():
    cnt = 0
    
    for i in range(10):
        cnt += 1
    
    l = [i for i in range(10) if i % 2]

    return l


answer = funcion()
print(answer)
