

from generalfunctions import projectdetails
from arquivefunctions import setfiles, importcarsbd, importclientsbd, importaddressbd, importrentbd
from menu import menu

#   Configura as Variáveis para o início do programa
#   As Essas Funções são explicadas em 'arquivefunctions.py'

setfiles()
carsbd = importcarsbd()
clientsbd = importclientsbd()
addressbd = importaddressbd()
rentbd = importrentbd()



if __name__ == '__main__':
    #   Inicia o Programa
    projectdetails()
    menu()
