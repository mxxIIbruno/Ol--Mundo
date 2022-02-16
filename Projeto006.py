class Cliente:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade


condição  = True

while condição:
    cont = 0

    while True:
        from string import ascii_letters
        
        nome =  str(input('Nome completo: '))

        for letra in nome:
            if letra in ascii_letters + ' ':
                cont += 1
            else:
                print('Não')
        
        if cont == len(nome):
            nome = nome.split()
            break
    
    while True:
        email = str(input('E-mail: '))

        conta = ['@gmail.com','@hotmail.com','@outlook.com']
        
        arroba = email.find('@')
        com = email.find('com')
        
        parte_email = email[arroba:com+3]
        
        if parte_email in conta:
            break
        else:
            print('Email Invalido')

    while True:
        idade = int(input('Idade: '))

        if 18 <= idade <= 100:
            break
        else:
            print('Tente denovo!')

    nome = nome[0] + ' ' + nome[-1]
    condição = False

dado = Cliente(nome=nome, email=email, idade=idade)

dados = {
    'nome':dado.nome,
    'email':dado.email,
    'idade':dado.idade
}

print('\nConta Aprovada\n')
for k,v in dados.items():
    print(f'{k}: {v}')
