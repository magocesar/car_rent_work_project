

def projectdetails():
    from time import sleep
    participants = ('Bernardo Lima Hack',
                    'César Willian Pacheco',
                    'Gabriela Ribeiro',
                    'Otávio Carneiro Nogueira',
                    'Rodrigo Münch')
    print('-=-' * 10)
    print('PROJETO LOCALIZA'.center(30))
    sleep(.5)
    print('BES - 2022 - 1'.center(30))
    sleep(.5)
    print('-=-' * 10)
    sleep(.5)
    print('PARTICIPANTES:'.center(30))
    sleep(.5)
    for participant in participants:
        print(participant.center(30))
        sleep(.5)
    print('-=-' * 10)


def client_register():
    from time import sleep
    from main import clientsbd
    from datetime import date
    print('-=-' * 10)
    while True:
        try:
            cpf = str(input('Digite o CPF do Cliente: ')).strip().upper()
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    while True:
        try:
            name = str(input('Digite o Nome do Cliente: ')).strip().upper()
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    while True:
        try:
            day = int(input('Digite o Dia de Nascimento do CLiente: '))
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    while True:
        try:
            month = int(input('Digite o Mês de Nascimento do CLiente: '))
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    while True:
        try:
            year = int(input('Digite o Ano de Nascimento do CLiente: '))
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    find = False
    for client in clientsbd:
        if client['CPF DO CLIENTE'] == cpf:
            find = True
            print('CPF já Cadastrado no Banco de Dados')
            print('-=-' * 10)
            sleep(1)
    if not find:
        age = calculateAge(date(year, month, day))
        if age < 18:
            print('O Cliente é Menor de 18 Anos, Não é Possível Cadastra-lo')
            print('-=-' * 10)
            sleep(1)
        else:
            if month < 10:
                month_final = '0' + str(month)
            else:
                month_final = month
            print('Cliente Adicionado no Banco de Dados!')
            print('-=-' * 10)
            sleep(1)
            return {'NOME DO CLIENTE': name, 'CPF DO CLIENTE': cpf, 'IDADE DO CLIENTE': age, 'DATA DE NASCIMENTO': f'{day}/{month_final}/{year}'}


def car_register():
    from time import sleep
    from main import carsbd
    print('-=-' * 10)
    while True:
        try:
            manufactor = str(input('Digite a Fabricante do Carro: ')).strip().upper()
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    while True:
        try:
            model = str(input('Digite o Modelo do Carro: ')).strip().upper()
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    while True:
        try:
            year = str(input('Digite o Ano de Fabricação do Carro: ').strip().upper())
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    while True:
        try:
            color = str(input('Digite a Cor do Carro: ')).strip().upper()
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    while True:
        try:
            plate = str(input('Digite a Placa do Carro: ')).strip().upper()
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    find = False
    for car in carsbd:
        if car['PLACA'] == plate:
            find = True
            print('Placa Já Cadastrada no Banco de Dados')
            print('-=-' * 10)
            sleep(1)
    if not find:
        print('Carro Adicionado ao Banco de Dados!')
        print('-=-' * 10)
        sleep(1)
        return {'FABRICANTE': manufactor, 'MODELO': model, 'ANO': year, 'COR': color, 'PLACA': plate}


def client_city():
    from time import sleep
    from main import clientsbd
    while True:
        try:
            cpf = str(input('Digite o CPF do cliente: ')).strip().upper()
        except:
            print('ERRO')
        else:
            for client in clientsbd:
                if client['CPF DO CLIENTE'] == cpf:
                    while True:
                        try:
                            city = str(input('Digite a Cidade em que o Cliente Reside: ')).strip().upper()
                        except:
                            print('\33[31m Erro, Tente Novamente!\33[m')
                        else:
                            break
                    while True:
                        try:
                            adress = str(input('Digite seu Endereco: ')).strip().upper()
                        except:
                            print('\033[31m Erro, Tente Novamente\33[m')
                        else:
                            break
                    while True:
                        try:
                            cep = str(input('Digite o seu CEP: ')).strip().upper()
                        except:
                            print('\033[31m Erro, Tente Novamente\33[m')
                        else:
                            break
                    print('Endereço do Cliente Salvo com Sucesso!')
                    print('-=-' * 10)
                    sleep(1)
                    return {'CPF DO CLIENTE': client['CPF DO CLIENTE'], 'CIDADE DO CLIENTE': city, 'ENDEREÇO DO CLIENTE': adress, 'CEP DO CLIENTE': cep}
            print('Cliente não Encontrado, Cadastre Esse Cliente na Tela Inicial')
            print('-=-' * 10)
            sleep(1)


def rent_register():
    from main import clientsbd, carsbd, addressbd
    from time import sleep
    while True:
        try:
            cpf = str(input('Digite o CPF do Cliente: ')).strip().upper()
        except:
            print('\033[31Erro, Tente Novamente.\033[m')
        else:
            break
    find = False
    for data in clientsbd:
        if data['CPF DO CLIENTE'] == cpf:
            find = True
    if not find:
        print('Cliente Não Cadastrado no Banco de Dados, Cadastre o Cliente na Tela Inicial.')
        print('-=-' * 10)
        sleep(1)

    if find:

        while True:
            try:
                plate = str(input('Digite a Placa do Carro: ')).strip().upper()
            except:
                print('\033[31mErro, Tente Novamente.\033[m')
            else:
                break
        find = False
        for data in carsbd:
            if data['PLACA'] == plate:
                find = True
        if not find:
            print('Carro não Cadastrado no Banco de Dados, Cadastre o Carro na Tela Inicial.')
            print('-=-' * 10)
            sleep(1)

        if find:

            for data in clientsbd:
                if data['CPF DO CLIENTE'] == cpf:
                    final_cpf = cpf
                    name = data['NOME DO CLIENTE']
                    age = data['IDADE DO CLIENTE']

            for data in carsbd:
                if data['PLACA'] == plate:
                    final_plate = plate
                    model = data['MODELO']
                    color = data['COR']
                    manufactor = data['FABRICANTE']

            for data in addressbd:
                if data['CPF DO CLIENTE'] == cpf:
                    city = data['CIDADE DO CLIENTE']

            print('Dados do Aluguel Cadastrados com Sucesso no Banco de Dados!')
            print('-=-' * 10)
            sleep(1)
            return {'NOME DO CLIENTE': name, 'CPF DO CLIENTE': final_cpf, 'IDADE DO CLIENTE': age, 'CIDADE DO CLIENTE': city,
                    'FABRICANTE DO CARRO': manufactor, 'MODELO DO CARRO': model, 'COR DO CARRO': color, 'PLACA DO CARRO': final_plate}


def showcars():
    from main import carsbd
    from time import sleep
    if not carsbd:
        print('Nenhum Carro Foi Cadastrado no Banco de Dados')
        print('-=-' * 10)
        sleep(1)
    else:
        counter = 1
        for data in carsbd:
            print(f'CADASTRO {counter}'.center(30))
            print(data)
            counter += 1
        print('-=-' * 10)


def showclients():
    from main import clientsbd
    from time import sleep
    if not clientsbd:
        print('Nenhum Cliente Foi Cadastrado no Banco de Dados')
        print('-=-' * 10)
        sleep(1)
    else:
        counter = 1
        for data in clientsbd:
            print(f'CADASTRO {counter}'.center(30))
            print(data)
            counter += 1
        print('-=-' * 10)


def showcitys():
    from main import addressbd
    from time import sleep
    if not addressbd:
        print('Nenhum Endereço Foi Cadastrado no Banco de Dados')
        print('-=-' * 10)
        sleep(1)
    else:
        counter = 1
        for data in addressbd:
            print(f'CADASTRO {counter}'.center(30))
            print(data)
            counter += 1
        print('-=-' * 10)


def showrents():
    from main import rentbd
    from time import sleep
    if not rentbd:
        print('Nenhum Endereço Foi Cadastrado no Banco de Dados')
        print('-=-' * 10)
        sleep(1)
    else:
        counter = 1
        for data in rentbd:
            print(f'CADASTRO {counter}'.center(30))
            print(data)
            counter += 1
        print('-=-' * 10)


def erase():
    from main import carsbd, clientsbd, addressbd, rentbd
    from time import sleep
    ops = ('[1] - Carro',
           '[2] - Cliente',
           '[3] - Endereço',
           '[4] - Aluguel',
           '[5] - Voltar')
    print('-=-' * 10)
    print('APAGAR DO BANCO DE DADOS'.center(30))
    for op in ops:
        print(op)
    print('-=-' * 10)
    while True:
        try:
            q = int(input('Digite uma Opção Válida: '))
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            if q not in [1, 2, 3, 4, 5]:
                print('\033[31mDigite uma Opção Válida.\033[m')
                print('-=-' * 10)
                sleep(1)
            else:
                break
    if q == 1:
        if not carsbd:
            print('Nenhum Carro Foi Cadastrado.')
            print('-=-' * 10)
            sleep(1)
        else:
            erasecar()
    elif q == 2:
        if not clientsbd:
            print('Nenhum Cliente Foi Cadastrado.')
            print('-=-' * 10)
            sleep(1)
        else:
            eraseclient()
    elif q == 3:
        if not addressbd:
            print('Nenhum Endereço Foi Cadastrado.')
            print('-=-' * 10)
            sleep(1)
        else:
            eraseaddress()
    elif q == 4:
        if not rentbd:
            print('Nenhum Aluguel Foi Cadastrado.')
            print('-=-' * 10)
            sleep(1)
        else:
            eraserent()
    elif q == 5:
        print('Retonando ao Menu Principal...')
        print('-=-' * 10)
        sleep(1)


def eraseclient():
    from main import clientsbd
    from time import sleep
    while True:
        try:
            cpf = str(input('Digite o CPF do Cliente ')).strip().upper()
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    find = False
    for counter, data in enumerate(clientsbd):
        if data['CPF DO CLIENTE'] == cpf:
            find = True
            clientsbd.pop(counter)
            print('Dados do Cliente Foram Deletados do Banco de Dados')
            print('-=-' * 10)
            sleep(1)
    if not find:
        print('CPF não Encontrado no Banco de Dados.')
        print('-=-' * 10)
        sleep(1)


def erasecar():
    from main import carsbd
    from time import sleep
    while True:
        try:
            plate = str(input('Digite a Placa do Carro ')).strip().upper()
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    find = False
    for counter, data in enumerate(carsbd):
        if data['PLACA'] == plate:
            find = True
            carsbd.pop(counter)
            print('Dados do Carro Foram Deletados do Banco de Dados')
            print('-=-' * 10)
            sleep(1)
    if not find:
        print('Carro não Encontrado no Banco de Dados')
        print('-=-' * 10)
        sleep(1)


def eraseaddress():
    from main import addressbd
    from time import sleep
    while True:
        try:
            cpf = str(input('Digite o CPF do Cliente ')).strip().upper()
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    for counter, data in enumerate(addressbd):
        if data['CPF DO CLIENTE'] == cpf:
            find = True
            addressbd.pop(counter)
            print('Endereço do Cliente Deletado do Banco de Dados.')
            print('-=-' * 10)
            sleep(1)
    if not find:
        print('Endereço não Encontrado no Banco de Dadosd.')
        print('-=-' * 10)
        sleep(1)


def eraserent():
    from main import rentbd
    from time import sleep
    while True:
        try:
            cpf = str(input('Digite o CPF do Cliente ')).strip().upper()
        except:
            print('\033[31mErro, Tente Novamente.\033[m')
        else:
            break
    for counter, data in enumerate(rentbd):
        if data['CPF DO CLIENTE'] == cpf:
            find = True
            rentbd.pop(counter)
            print('Aluguel do Cliente Deletado do Banco de Dados.')
            print('-=-' * 10)
            sleep(1)
    if not find:
        print('Aluguel não Encontrado no Banco de Dados.')
        print('-=-' * 10)
        sleep(1)


def especific_client():
    from main import clientsbd
    from time import sleep
    if not clientsbd:
        print('Nenhum Cliente Cadastrado no Banco de Dados')
        print('-=-' * 10)
        sleep(1)
    else:
        while True:
            try:
                cpf = str(input('Digite o CPF do Cliente ')).strip().upper()
            except ValueError:
                print('\033[31mErro, Tente Novamente\033[m')
            else:
                break
        find = False
        for client in clientsbd:
            if client['CPF DO CLIENTE'] == cpf:
                find = True
                print('Dados do Carro: ')
                print(client)
                sleep(1)
        if not find:
            print('Cliente não Cadastrado no Banco de Dados')
            print('-=-' * 10)
            sleep(1)
        


def especific_car():
    from main import carsbd
    from time import sleep
    if not carsbd:
        print('Nenhum Carro Cadastrado no Banco de Dados')
        print('-=-' * 10)
        sleep(1)
    else:
        while True:
            try:
                plate = str(input('Digite a Placa do Carro ')).strip().upper()
            except ValueError:
                print('\033[31mErro, Tente Novamente\033[m')
            else:
                break
        find = False
        for car in carsbd:
            if car['PLACA'] == plate:
                find = True
                print('Dados do Carro: ')
                print(car)
                sleep(1)
        if not find:
            print('Placa não Cadastrada no Banco de Dados')
            print('-=-' * 10)
            sleep(1)
    
def calculateAge(born): 
    from datetime import date
    today = date.today() 
    try:  
        birthday = born.replace(year = today.year) 
    except ValueError:  
        birthday = born.replace(year = today.year, 
                  month = born.month + 1, day = 1) 
    if birthday > today: 
        return today.year - born.year - 1
    else: 
        return today.year - born.year 




if __name__ == '__main__':
    pass
