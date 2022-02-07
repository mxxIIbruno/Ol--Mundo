class Calendario:
    def __init__(self):
        pass
    
    def _Letra(self, mensagem):
        from time import sleep

        for letra in str(mensagem):
            sleep(0.1)
            print(letra, end='', flush=True)
        print()
    
    def _Atual(self):
        from datetime import date
        
        ano = date.today().year
        mes = date.today().month
        dia = date.today().day
        
        data = {
            'Ano':ano,
            'Mês':mes,
            'Dia':dia
            }

        return data  
    
    def _Bissexto(self, ano, apresentar=True):
        if int(ano) % 4 == 0 and int(ano) % 100 != 0 or int(ano) % 400 == 0:
            fev = 29
        else:
            fev = 28
        
        meses = [
            ['Janeiro','Fevereiro','Março','Abril','Maio','Junho',
            'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'],
            [31,fev,31,30,31,30,31,31,30,31,30,31]
            ]
        
        if apresentar==True:
            hoje = self._Atual()

            print('\n'+' '*15, end='')                                                              # Apresentação da Data Atual Parte 1
            self._Letra(f'Hoje é {hoje["Dia"]} de {meses[0][hoje["Mês"]-1]} de {hoje["Ano"]}')       # Apresentação da Data Atual Parte 2

        return meses
    
    def _Nascimento(self):
        hoje = self._Atual()
        
        while True:
            ano = int(input('\nAno de Nascimento: '))

            if 1500 <= ano <= hoje['Ano']:
                self._Letra(f'Muito Bom...\nVocê Nasceu em {ano}')
                break
            else:
                print(f'Um ano entre 1500 e {hoje["Ano"]}...')
        
        anoBi = self._Bissexto(ano, apresentar=False)

        while True:
            mes = int(input('\nMês do Nascimento: '))                                     # Mes de Nascimento do Cliente
            
            if 1 <= mes <= 12:
                self._Letra(f'Muito Bom...\nVocê Nasceu em {anoBi[0][mes-1]}')
                break
            else:
                print('Referente ao mês do nascimento\nTente de 1 a 12.')

        while True:
            mes_cliente = anoBi[1][mes-1]
            dia = int(input('\nDia do Nascimento: '))
            
            if 1 <= dia <= mes_cliente:
                self._Letra(f'Muito Bom...\nVocê Nasceu no dia {dia}')
                break
            else:
                print(f'O dia do seu nascimento:\nDe 1 á {mes_cliente}')

        data_nascimento = {
            'Ano':ano,
            'Mês':mes,
            'Dia':dia
            }
        
        return data_nascimento

    def _Fase_Final(self, ano, mes, dia):
        hoje = self._Atual()
        meses = self._Bissexto(hoje['Ano'], apresentar=False)
        
        idade_ano = hoje['Ano'] - ano
        idade_mes = hoje['Mês'] - mes
                
        if idade_mes < 0:
            idade_ano -= 1
            
            if hoje['Dia'] >= dia:
                idade_mes += 12
            else:
                idade_mes += 11
            
            idade_dia = hoje['Dia'] - dia

        elif idade_mes == 0:
            if hoje['Dia'] >= dia:
                idade_dia = hoje['Dia'] - dia
            else:
                idade_ano -= 1
                idade_mes += 11
                idade_dia = meses[1][hoje['Mês']-2] - dia
        else:
            if hoje['Dia'] >= dia:
                idade_dia = hoje['Dia'] - dia
            else:
                idade_mes -= 1
                idade_dia = meses[1][hoje['Mês']-2] - dia
                
        idade = {
            'Ano':idade_ano,
            'Mês':idade_mes,
            'Dia':idade_dia
        }

        return idade
