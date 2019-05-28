# -*- coding: utf-8 -*-

pessoas = [
    {
        "id": 1,
        "nome": "Luan",
        "email": "luan@github.com.br"
    },
    {
        "id": 2,
        "nome": "Teste",
        "email": "alo@mundo"
    }
]

f = open('./cache/file.txt', 'w')

for pessoa in pessoas:
    f.write("ID: " + str(pessoa["id"]) + "\n")
    f.write("Nome: " + pessoa["nome"] + "\n")
    f.write("E-mail: " + pessoa["email"] + "\n")
    f.write("-----------------\n")

    print("Nome: " + pessoa["nome"])
    print("E-mail: " + pessoa["email"])

print(pessoas)



#f.write("Ola Mundo!\n")
#f.write('Olá Mundo 2')
f.close()
