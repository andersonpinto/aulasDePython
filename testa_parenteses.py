a="()()()()"
b = list(a)

while True:
    abertos = a.count("(")
    fechados = a.count(")")
    if abertos != fechados:
        print("deixou algum aberto")
        break
    elif a[-1] != ")":
        print("só pelo ultimo já dava para saber que falta fechar")
        break
    else:
        b.pop(-1)*2
        if b == []:
            break
    
print(b)
