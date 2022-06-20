import pickle


def menu():
    from main import carsbd, clientsbd, addressbd, rentbd
    import generalfunctions
    from time import sleep
    from arquivefunctions import ending_program
    ops = ('[1] - Cadastrar Carro de Aluguel.',
           '[2] - Cadastrar Cliente.',
           '[3] - Cadastrar Cidade do Cliente.',
           '[4] - Cadastrar Novo Aluguel.',
           '[5] - Mostrar Carros Cadastrados.',
           '[6] - Mostrar Clientes Cadastrados.',
           '[7] - Mostrar Cidades Cadastradas.',
           '[8] - Mostrar Alugueis',
           '[9] - Mostrar Cliente Específico',
           '[10] - Mostrar Carro Específico',
           '[11] - Apagar Dados.',
           '[12] - Encerrar Programa.')
    while True:
        print('OPERAÇÕES:'.center(30))
        for op in ops:
            print(op)
        print('-=-' * 10)
        try:
            question = int(input('Digite uma Opção Válida! '))
        except ValueError:
            print('\033[31mDigite um Valor Inteiro!\033[m')
        else:
            if question not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                print('\033[31mPor Favor, Digite uma Opção Válida!\033[m')
                print('-=-' * 10)
                sleep(1)
            else:
                if question == 1:
                    result = generalfunctions.car_register()
                    if result is None:
                        pass
                    else:
                        carsbd.append(result)
                elif question == 2:
                    result = generalfunctions.client_register()
                    if result is None:
                        pass
                    else:
                        clientsbd.append(result)
                elif question == 3:
                    addressbd.append(generalfunctions.client_city())
                    print('-=-' * 10)
                elif question == 4:
                    result = generalfunctions.rent_register()
                    if result is None:
                        pass
                    else:
                        rentbd.append(result)
                elif question == 5:
                    generalfunctions.showcars()
                elif question == 6:
                    generalfunctions.showclients()
                elif question == 7:
                    generalfunctions.showcitys()
                elif question == 8:
                    generalfunctions.showrents()
                elif question == 9:
                    generalfunctions.especific_client()
                elif question == 10:
                    generalfunctions.especific_car()
                elif question == 11:
                    generalfunctions.erase()
                elif question == 12:
                    ending_program()
                    print('Até Breve')
                    sleep(1)
                    break








