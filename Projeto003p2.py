# Importando meu projeto
from Projeto003p1 import Calendario
from datetime import date

base = Calendario()                                                                     # Chamar a Classe

hoje = base._Atual()                                                                    # Hoje Atual em um Dicionario
lista = base._Bissexto(hoje['Ano'])                                                     # Ver se o ano é bissexto

nascimento = base._Nascimento()
idade_cliente = base._Fase_Final(nascimento['Ano'],nascimento['Mês'],nascimento['Dia'])

print(f'\nVocê tem {idade_cliente["Ano"]} Ano(s) {idade_cliente["Mês"]} Mês(es) {idade_cliente["Dia"]} Dia(s)')

dias = date.today() - date(nascimento['Ano'], nascimento['Mês'], nascimento['Dia'])

print(f'Totalizando {dias} dias\n')
