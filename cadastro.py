
while True:
    print("===========")
    print("sistema de cadastro")
    print("============")

    print("1 - cadastrar")
    print("2 - fazer login")
    print("3 - sair")

    opcao = int(input("escolha uma opção:"))
#funcionalidades
    #se o usuario digitar o valor 1, vai ser exebido
    # a ação abaixo:
    if(opcao == 1) :
        print("=====teela de cadastro=====")
        print("=========================")
    elif (opcao == 2 ):
        print("================")
        print("===tela de login===")
        print("==============")

    else:
        print("você está saindo do cadastro, até mais!")
        break