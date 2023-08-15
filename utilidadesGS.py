"""
Página para a criação das funções que serão utilizadas no nosso programa
"""

import webbrowser as wb

agricultores = []
tarefas = []


def leiaInt(msg):
    """
    Função que lê a opção desejada e se a opção não estiver correta
    ela retorna uma mensagem de erro.
    :param msg: int
    :return: string
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\n\33[31mERRO! Por favor, digite um número inteiro válido.\33[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return n


def linha(tam=55):
    """
    Função que cria uma linha para dividir o menu
    :param tam: int (quantidade de caracteres)
    :return: string (caracteres)
    """
    return "\033[32m-\033[m" * tam


def cabecalho(txt):
    """
    Função que cria um cabecalho entre duas linhas
    :param txt: string (texto que vai aparecer entre as linhas)
    :return: string (cabeçalho com o texto do parâmetro)
    """
    print(linha())
    print(txt.center(55))
    print(linha())


def menu(lista):
    """
    Função que cria uma lista com a quantidade de argumentos escolhidos
    :param lista: strings (opções do menu)
    :return: int (itens do menu) e string (nome dos itens do menu)
    """
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[32m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt(f"\033[32mDigite o número correspondente a sua opção:\033[m ")
    return opc


""" FUNÇÕES PARA A PRIMEIRA OPÇÃO DO MENU (CADASTRO)"""


def cadastrar_agricultor():
    """
    Função que cadastra o agricultor recebendo os dados como nome, cpf, telefone e email
    :return: string (agricultor)
    """
    cabecalho("\033[032mCADASTRO DE AGRICULTOR\033[m")
    nome = input("\033[032mDigite o seu nome completo:\033[m ")
    cpf = input("\033[032mDigite o seu cpf (somente os números, sem espaços ou caracteres especiais):\033[m ")
    telefone = input("\033[032mDigite o seu telefone(somente os números, sem espaços ou caracteres especiais):\033[m ")
    email = input("\033[032mDigite o seu email:\033[m ")
    agricultor = {
        'nome': nome,
        'cpf': cpf,
        'telefone': telefone,
        'email': email
    }
    agricultores.append(agricultor)
    print(f"\033[032m{nome} o seu cadastro foi realizado com sucesso!!\033[m")
    return agricultor


def atualizar_cadastro():
    """
    Função que atualiza os dados do agricultor cadastrado
    :return: String (dados atualizados)
    """
    cabecalho("\033[032mATUALIZAR CADASTRO\033[m")
    cpf = input("\033[032mDigite o CPF do cliente que deseja atualizar (somente os números, sem caracteres):\033[m ")
    atualizado = False
    for agricultor in agricultores:
        if agricultor['cpf'] == cpf:
            novo_nome = input("\033[032mDigite o novo nome:\033[m ")
            novo_telefone = input("\033[032mDigite o novo telefone:\033[m ")
            novo_email = input("\033[032mDigite o novo email:\033[m ")
            agricultor['nome'] = novo_nome
            agricultor['telefone'] = novo_telefone
            agricultor['email'] = novo_email
            print("\033[032mDados do agricultor atualizados com sucesso!\033[m")
            atualizado = True
            break
    if not atualizado:
        print("\033[31mAgricultor não encontrado.\033[m")
        print("")
        print("\033[032mDeseja realizar o cadastro ? (Digite o numero inteiro correspondente a sua escolha)\033[m")
        resposta = menu(["Sim", "Não"])
        if resposta == 1:
            cadastrar_agricultor()
        if resposta == 2:
            return


def consultar_cadastro():
    """
    Função que consulta os dados do agricultor cadastrado
    :return: String (dados do agricultor)
    """
    cabecalho("\033[032mCONSULTAR CADASTRO\033[m")
    cpf = input("\033[032mDigite o CPF do agricultor que deseja consultar (somente os números, sem caracteres): \033[m")
    encontrado = False
    for agricultor in agricultores:
        if agricultor['cpf'] == cpf:
            for key in agricultor.keys():

                print(f"\033[032m{key} - {agricultor[key]}")
            encontrado = True
            break
    if not encontrado:
        print("\033[31mCPF não cadastrado.\033[m")
        print("")
        print("\033[032mDeseja realizar o cadastro ? (Digite o numero inteiro correspondente a sua escolha)\033[m")
        resposta = menu(["Sim", "Não"])
        if resposta == 1:
            cadastrar_agricultor()
        if resposta == 2:
            return


def remover_cadastro():
    """
    Função que remove agricultor cadastrado
    :return: String (remove agricultor)
    """
    cabecalho("\033[032mREMOVER CADASTRO\033[m")
    cpf = input("\033[032mDigite o CPF do agricultor que deseja remover (somente os números, sem caracteres):\033[m ")
    removido = False
    for agricultor in agricultores:
        if agricultor['cpf'] == cpf:
            agricultores.remove(agricultor)
            print("\033[032mCadastro removido com sucesso!!!\033[m")
            removido = True
            break
    if not removido:
        print("\033[31mAgricultor não encontrado.\033[m")
        return


def menu_cadastro():
    """
    Função que cria um menu com as funções de cadastrar agricultor, atualizar cadastro,
    consultar cadastro e remover cadastro
    :return: Função escolhida
    """
    while True:
        cabecalho("\033[032mCADASTRO\033[m")
        resposta = menu(["Cadastrar Agricultor", "Atualizar Cadastro", "Consultar Cadastro", "Remover Cadastro",
                         "Voltar ao Menu Anterior"])
        if resposta == 1:
            cadastrar_agricultor()
            break
        elif resposta == 2:
            atualizar_cadastro()
            break
        elif resposta == 3:
            consultar_cadastro()
            break
        elif resposta == 4:
            remover_cadastro()
            break
        elif resposta == 5:
            return
        else:
            print("\033[31mERRO! Digite uma opção válida\033[m")


""" FUNÇÕES PARA A SEGUNDA OPÇÃO DO MENU (GERENCIADOR DE TAREFAS)"""


def cadastrar_tarefa():
    """
    Função que cadastra uma tarefa recebendo os dados como nome, tipo e descrição
    :return: string (tarefa)
    """
    cabecalho("\033[032mCADASTRO DE TAREFAS\033[m")
    cpf = input("\033[032mDigite o seu cpf (somente os números, sem espaços ou caracteres especiais):\033[m ")
    cadastrado = False
    for agricultor in agricultores:
        if agricultor['cpf'] == cpf:
            nome_tarefa = input("\033[032mDigite o nome da tarefa (Exemplo: Plantar Alface)")
            tipo = input("\033[032mDigite o tipo da tarefa (Exemplo: Plantio ou Colheita)")
            descricao = input("\033[032mDigite a descrição da Tarefa (Interessante colocar deveres,"
                              " data de início e data de fim): ")
            tarefa = {
                'cpf': cpf,
                'Nome': nome_tarefa,
                'Tipo': tipo,
                'Descrição': descricao,

            }
            tarefas.append(tarefa)
            print(f"\033[032mSua tarefa foi cadastrada com sucesso!!\033[m")
            return tarefa
    if not cadastrado:
        print("\033[31mCPF não cadastrado.\033[m")
        print("")
        print("\033[032mDeseja realizar o cadastro ? (Digite o numero inteiro correspondente a sua escolha)\033[m")
        resposta = menu(["Sim", "Não"])
        if resposta == 1:
            cadastrar_agricultor()
        if resposta == 2:
            return


def consultar_tarefa():
    """
    Função que consulta e mostra as tarefas cadastradas pelo usuário através
    do cpf
    :return: (String) Tarefas cadastradas
    """
    cabecalho("\033[032mCONSULTAR TAREFA\033[m")
    cpf = input("\033[032mDigite o CPF do agricultor que deseja consultar a tarefa"
                " (somente os números, sem caracteres): ")
    cadastro = False
    for agricultor in agricultores:
        if agricultor['cpf'] == cpf:
            cadastro = True
            cabecalho("\033[032mTAREFAS EXISTENTES\033[m")
            i = 1
            existente = False
            for tarefa in tarefas:
                if tarefa["cpf"] == cpf:
                    print(f"\033[032m{i}ª TAREFA")
                    i += 1
                    for key in tarefa.keys():
                        print(f"\033[032m{key} - {tarefa[key]}")
                    print("")
                    existente = True
            if not existente:
                print("\033[31mCPF não tem tarefa cadastrada.\033[m")
                print("")
                print("\033[032mDeseja realizar o cadastro de tarefas ? "
                      "(Digite o numero inteiro correspondente a sua escolha)\033[m")
                resposta = menu(["Sim", "Não"])
                if resposta == 1:
                    cadastrar_tarefa()
                if resposta == 2:
                    return
                return
    if not cadastro:
        print("\033[31mCPF não cadastrado.\033[m")
        print("")
        print("\033[032mDeseja realizar o cadastro ? "
              "(Digite o numero inteiro correspondente a sua escolha)\033[m")
        resposta = menu(["Sim", "Não"])
        if resposta == 1:
            cadastrar_agricultor()
        if resposta == 2:
            return


def remover_tarefa():
    """
    Função que consulta as tarefas através do cpf e remove a tarefa que o usuário escolher
    :return: Remove a tarefa escolhida pelo usuário
    """
    cabecalho("\033[032mREMOVER TAREFA\033[m")
    cpf = input("\033[032mDigite o CPF do agricultor que deseja remover a tarefa"
                " (somente os números, sem caracteres): ")
    cadastro = False
    for agricultor in agricultores:
        if agricultor['cpf'] == cpf:
            cadastro = True
            cabecalho("\033[032mTAREFAS EXISTENTES\033[m")
            i = 1
            existente = False
            for tarefa in tarefas:
                if tarefa["cpf"] == cpf:
                    print(f"\033[032m{i}ª TAREFA")
                    i += 1
                    for key in tarefa.keys():
                        print(f"\033[032m{key} - {tarefa[key]}")
                    print("")
                    existente = True
            if not existente:
                print("\033[31mCPF não tem tarefa cadastrada.\033[m")
                return
    if not cadastro:
        print("\033[31mCPF não cadastrado.\033[m")
        return
    while True:
        titulo = int(input("\033[032mDigite o numero da tarefa que deseja remover"
                           "(o numero deverá ser inteiro e exatamente igual ao da tarefa"
                           " não colocar 'ª' e nenhum outro caracter)\033[m"))
        if 0 < titulo < i:
            break
        print("\033[031mVocê digitou uma tarefa inexistente")
    titulo -= 1

    while True:
        if tarefas[titulo]['cpf'] == cpf:
            del (tarefas[titulo])
            print("\033[032mTarefa removida com sucesso!!!")
            break
        else:
            titulo += 1


def menu_tarefa():
    """
    Função que cria um menu com as opções Cadastrar Tarefa, Consultar Tarefa, Remover Tarefa e
    Voltar ao Menu Anterior
    :return: Retorna a opção escolhida
    """
    while True:
        cabecalho("\033[032mTAREFAS\033[m")
        resposta = menu(["Cadastrar Tarefa", "Consultar Tarefa", "Remover Tarefa",
                         "Voltar ao Menu Anterior"])
        if resposta == 1:
            cadastrar_tarefa()
            break
        elif resposta == 2:
            consultar_tarefa()
            break
        elif resposta == 3:
            remover_tarefa()
            break
        elif resposta == 4:
            return
        else:
            print("\033[31mERRO! Digite uma opção válida\033[m")


""" FUNÇÕES PARA A TERCEIRA OPÇÃO DO MENU (ONGs e PROJETOS SOCIAIS)"""


def consultar_ong():
    """
    Função que cria um menu com o nome de ONGs e Projetos Sociais dando a possibilidade do usuário saber
    mais sobre as instituições e posteriormente entrar no site da opção escolhida
    :return: Opção escolhida (Informações e Direcionamento ao Site)
    """
    while True:
        cabecalho("\033[032mONGs E PROJETOS SOCIAIS\033[m")
        resposta = menu(["Brasil Sem Fome", "ActionAid", "Anjos da Noite", "Outras", "Voltar ao Menu Anterior"])
        if resposta == 1:
            cabecalho("\033[032mPROJETO BRASIL SEM FOME\033[m")
            print("\033[32mFundada pelo sociólogo Herbert de Souza, o Betinho, \na Ação da Cidadania nasceu em 1993,"
                  "\033[32mformando uma \nimensa rede de mobilização de alcance nacional para \najudar 32 milhões de "
                  "\033[32mbrasileiros que, segundo dados \ndo Ipea, estavam abaixo da linha da pobreza. \nCriada no "
                  "\033[32mauge do Movimento pela Ética na Política, \na Ação da Cidadania contra a Fome, a Miséria "
                  "\033[32me pela \nVida se transformou no movimento social mais \nreconhecido do Brasil. \nSeu "
                  "\033[32mprincipal eixo de atuação é uma extensa rede de \nmobilização formada por "
                  "\033[32mcomitês locais da sociedade \ncivil organizada, em sua maioria compostos por \nlideranças"
                  "\033[32m comunitárias, mas com participação de \ntodos os setores sociais.")
            opcao = menu(["Acessar Site", "Sair"])
            if opcao == 1:
                wb.open("https://www.brasilsemfome.org.br/")
                break
            elif opcao == 2:
                break
            else:
                print("\033[31mERRO! Digite uma opção válida\033[m")
        elif resposta == 2:
            cabecalho("\033[032mACTIONAID\033[m")
            print("\033[32mApoia na construção de hortas comunitárias e \nagroecológicas que fazem com que crianças"
                  "\033[32m e toda a\ncomunidade tenham acesso a uma alimentação segura \ne de qualidade."
                  "\033[32m \nEste tipo de produção é sustentável, responsável \ncom o solo, água e florestas,"
                  "\033[32m preserva as sementes \nnativas e diversifica o cultivo. Estas são ações que \ngarantem "
                  "\033[32mo consumo próprio e a geração de renda de\ntoda a comunidade.")
            opcao = menu(["Acessar Site", "Sair"])
            if opcao == 1:
                wb.open("https://seguro.actionaid.org.br/")
                break
            elif opcao == 2:
                break
            else:
                print("\033[31mERRO! Digite uma opção válida\033[m")
            break
        elif resposta == 3:
            cabecalho("\033[032mANJOS DA NOITE\033[m")
            print("\033[32mFundado por Kaká Ferreira e José Amato, o Núcleo \nAssistencial Anjos da Noite realiza o"
                  "\033[32mtrabalho \ndesde 22 de agosto de 1989. É composto por pessoas \nde todas as idades, "
                  "\033[32mde várias denominações religiosas \nque voluntariamente doam, além do seu tempo,"
                  "\033[32m \nalimentos, roupas, agasalhos, calçados, cobertores \ne principalmente amor."
                  "\033[32m \nUma simples refeição, um agasalho e uma palavra amiga \nsão os ferramentas "
                  "\033[32mfundamentais para possibilitar \no resgate da autoestima objetivando a sua "
                  "\033[32m\nreintegração social.")
            opcao = menu(["Acessar Site", "Sair"])
            if opcao == 1:
                wb.open("http://www.anjosdanoite.org.br/doacoes.cfm")
                break
            elif opcao == 2:
                break
            else:
                print("\033[31mERRO! Digite uma opção válida\033[m")
            break
        elif resposta == 4:
            cabecalho("\033[032mSITE COM LISTA DE ONGs E PROJETOS SOCIAIS\033[m")
            opcao = menu(["Acessar Site", "Sair"])
            if opcao == 1:
                wb.open("https://g1.globo.com/fantastico/noticia/2021/04/04/"
                        "ajude-a-combater-a-fome-no-brasil-veja-lista-de-instituicoes.ghtml")
                break
            elif opcao == 2:
                break
            else:
                print("\033[31mERRO! Digite uma opção válida\033[m")
            break

        elif resposta == 5:
            return
        else:
            print("\033[31mERRO! Digite uma opção válida\033[m")


""" FUNÇÕES PARA A QUARTA OPÇÃO DO MENU (ORIENTAÇÕES AO AGRICULTOR)"""


def orientacoes_agro():
    """
    Função que cria um menu com as opções de Orientações de Plantio, Orientações de Colheita,
    Formas de Agricultura Sustentável, Previsões Climáticas e Voltar ao Menu Anterior.
    As Opções dão opção para o usuário entrar em um site que fala sobre o item da opção escolhida
    :return: Opção escolhida (Direcionamento para site da internet referente ao item escolhido)
    """
    while True:
        cabecalho("\033[032mORIENTAÇÕES AO AGRICULTOR\033[m")
        resposta = menu(["Orientações de Plantio", "Orientações de Colheita",
                         "Formas de Agricultura Sustentável", "Previsões Climáticas",
                         "Voltar ao Menu Anterior"])

        if resposta == 1:
            cabecalho("\033[032mORIENTAÇÕES DE PLANTIO")
            opcao = menu(["Acessar Site", "Sair"])
            if opcao == 1:
                wb.open("https://blog.syngentadigital.ag/cinco-dicas-para-um-plantio-eficiente/")
                break
            elif opcao == 2:
                break
            else:
                print("\033[31mERRO! Digite uma opção válida\033[m")
            break

        elif resposta == 2:
            cabecalho("\033[032mORIENTAÇÕES DE COLHEITA")
            opcao = menu(["Acessar Site", "Sair"])
            if opcao == 1:
                wb.open("https://www.sicredi.com.br/site/blog/"
                        "prejuizos-na-colheita-confira-6-dicas-para-reduzir-perdas/")
                break
            elif opcao == 2:
                break
            else:
                print("\033[31mERRO! Digite uma opção válida\033[m")
            break

        elif resposta == 3:
            cabecalho("\033[032mFORMAS DE AGRICULTURA SUSTENTÁVEL")
            opcao = menu(["Acessar Site", "Sair"])
            if opcao == 1:
                wb.open("https://www.sustainablecarbon.com/blog/5-praticas-sustentaveis-para-agricultura/")
                break
            elif opcao == 2:
                break
            else:
                print("\033[31mERRO! Digite uma opção válida\033[m")
            break

        elif resposta == 4:
            cabecalho("\033[032mPREVISÕES CLIMÁTICAS")
            opcao = menu(["Acessar Site", "Sair"])
            if opcao == 1:
                wb.open("https://www.climatempo.com.br/previsao-do-tempo?page=HOJE")
                break
            elif opcao == 2:
                break
            else:
                print("\033[31mERRO! Digite uma opção válida\033[m")
            break

        elif resposta == 5:
            return
        else:
            print("\033[31mERRO! Digite uma opção válida\033[m")
