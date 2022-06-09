import pickle


def menu():
    from main import carsbd, clientsbd, addressbd, rentbd
    import generalfunctions
    from time import sleep
    ops = ('[1] - Cadastrar Carro de Aluguel.',
           '[2] - Cadastrar Cliente.',
           '[3] - Cadastrar Cidade do Cliente.',
           '[4] - Cadastrar Novo Aluguel.',
           '[5] - Mostrar Carros Cadastrados.',
           '[6] - Mostrar Clientes Cadastrados.',
           '[7] - Mostrar Cidades Cadastradas.',
           '[8] - Mostrar Alugueis',
           '[9] - Apagar Dados.',
           '[10] - Encerrar Programa.')
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
            if question not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                print('\033[31mPor Favor, Digite uma Opção Válida!\033[m')
                print('-=-' * 10)
                sleep(1)
            else:
                if question == 1:
                    carsbd.append(generalfunctions.car_register())
                elif question == 2:
                    clientsbd.append(generalfunctions.client_register())
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
                    generalfunctions.erase()
                elif question == 10:
                    #   save clientbd
                    archive = open('clientsbd.txt', 'wb')
                    pickle.dump(clientsbd, archive)
                    archive.close()

                    #   save carsbd

                    archive = open('carsbd.txt', 'wb')
                    pickle.dump(carsbd, archive)
                    archive.close()

                    # save address

                    archive = open('addressbd.txt', 'wb')
                    pickle.dump(addressbd, archive)
                    archive.close()

                    #save rent

                    archive = open('rentbd.txt', 'wb')
                    pickle.dump(rentbd, archive)
                    archive.close()

                    print('Fim desse Inferno')
                    break