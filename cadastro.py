#variaveis para cadastro
nome = ""
idade = ""
usuario = ""
senha = ""
#apenas tela de visualização
while True:
    print("===========")
    print("sistema de cadastro")
    print("============")

    print("1 - cadastrar")
    print("2 - fazer login")
    print("3 - sair")

    opcao = input("escolha uma opção:")
#funcionalidades
    #se o usuario digitar o valor 1, vai ser exebido
    # a ação abaixo:
    if(opcao == "1") :
        print("=====teela de cadastro=====")
        print("=========================")
        nome = input("digite o seu nome: ")
        idade = input("digite a sua idade: ")
        usuario = input("digite o seu usuario: ")
        senha = ("digite a sua senha:") 
        print("\n cadastro realizado!\n")
   #se digitar  2, abre a tela de login
    elif (opcao == "2"):
        print("================")
        print("===tela de login===")
        print("==============")
        login_usurio = input("digite o usuario cadastrado: ")
        login_senha = input("digite a senha: ")
        
        #processamento de usuario e senha
        # if login_usuario == usuario and login_aenha == senha :

        #se digitar 3. sai da execucao
    elif(opcao == "3"):
        print("você está saindo do cadastro, até mais!") 
        # se nao for nem1,2 ou 3, mostrar erro e repetir o codigo
    else:
        print("valor digitado, invalido,use apenas numeros inteiros do menu")
        break 