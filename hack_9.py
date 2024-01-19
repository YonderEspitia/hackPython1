"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    nueva_lista = []
    i = 0
    while i < len(result):
        nueva_lista.append(result[i])
        nueva_lista.append('@')
        i += 1
   
    
    return nueva_lista

print(fn_hack_9())



