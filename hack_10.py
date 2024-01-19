"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
   
    result = "fooziman"
    lista=[]
    for letra in result:
        if letra == "o":
            lista.append("0")
        elif letra == "i":
            lista.append("1")
        elif letra == "a":
            lista.append("@")
        else:
            lista.append(letra.upper())

    return lista

print(fn_hack_10()) 


