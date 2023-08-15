"""
Página Principal do Programa
"""

from utilidadesGS import *

cabecalho("\033[032mBem vindo a IAgro\033[m")

while True:
    cabecalho("\033[032mMENU PRINCIPAL\033[m")
    resposta = menu(["Cadastro", "Gerenciador de Tarefas", "ONGs e Projetos Sociais",
                     "Orientações ao Agricultor", "Sair"])
    if resposta == 1:
        menu_cadastro()
    elif resposta == 2:
        menu_tarefa()
    elif resposta == 3:
        consultar_ong()
    elif resposta == 4:
        orientacoes_agro()
    elif resposta == 5:
        cabecalho("\033[032mSaindo do Programa... Até Logo!\033[m")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida\033[m")