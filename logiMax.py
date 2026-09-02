usuario = str(input('Seja Bem vindo a LogiMax, como posso ajudar?')).upper()

if usuario == 'ALTERAR DADOS' or usuario == 'TROCAR DADOS' or usuario == 'TROCAR MEUS DADOS' or usuario == 'ALTERAR MEUS DADOS':
    CPF = input('Digite seu CPF (somente números): ')
    while not (CPF.isdigit() and len(CPF) == 11):
        print('CPF Inválido, tente novamente. ')
        CPF = input('Digite seu CPF (somente números): ')
    else:
        NOME = str(input('Digite Seu Nome:'))
        CONFIRMAR_NOME = str(input('Confirma sua Alteração?')).upper()
        while CONFIRMAR_NOME == 'NAO' or CONFIRMAR_NOME == 'NÃO':
            NOME = str(input('Digite Seu Nome:'))
            CONFIRMAR_NOME = str(input('Confirma sua Alteração?')).upper()
        if CONFIRMAR_NOME == 'SIM':
            ENDERECO = str(input('Digite Seu endereço:'))
            NUMERO_ENDERECO = int(input('Digite o numero do endereço:'))
            CONFIRMAR_ENDERECO = str(input('Confirma o seu Endereço e numero?')).upper()
            while CONFIRMAR_ENDERECO == 'NAO' or CONFIRMAR_NOME == 'NÃO':
                ENDERECO = str(input('Digite Seu endereço:'))
                NUMERO_ENDERECO = int(input('Digite o numero da sua casa'))
                CONFIRMAR_ENDERECO = str(input('Confirma o seu Endereço e numero?')).upper()
                if CONFIRMAR_ENDERECO == 'SIM':
                    print('Dados confirmados, sua alteração foi realizada!')
                    TELEFONE = input('DIGITE SEU TELEFONE COM DDD (somente números): ')
                    CONFIRMAR_TELEFONE = str(input('CONFIRMA O NUMERO DE TELEFONE DIGITADO?'))
                    while not (TELEFONE.isdigit() and len(TELEFONE) == 11):
                        print('TELEFONE Inválido, tente novamente')
                        TELEFONE = input('Digite seu TELEFONE COM DDD (somente números): ')
                    else:
                        print('NÚMERO DE TELEFONE CONFIRMADO')
                        print('ESCOLHA SEU PROVEDOR DE E-MAIL')
                        print('[1] gmail.com')
                        print('[2] hotmail.com')
                        print('[3] yahoo.com.br')

                        PROVEDOR_EMAIL = int(input('DIGITE O NÚMERO DO SEU PROVEDOR: '))

                        email = input('DIGITE SEU EMAIL: ')
                        CONFIRMAR_EMAIL = input('CONFIRMA O E-MAIL DIGITADO? ').upper()

                        while CONFIRMAR_EMAIL in ('NAO', 'NÃO'):
                            email = input('DIGITE SEU E-MAIL: ')
                            CONFIRMAR_EMAIL = input('CONFIRMA O E-MAIL DIGITADO? ').upper()

elif usuario == 'CADASTRAR' or usuario == ' CADASTRAR CONTA' or usuario == 'CADASTRAR MINHA CONTA':

    # CPF = input('Digite seu CPF (somente números): ')
    #while not (CPF.isdigit() and len(CPF) == 11):
     #   print('CPF Inválido, tente novamente')
      #  CPF = input('Digite seu CPF (somente números): ')
    #else:
     #   NOME = str(input('Digite Seu Nome:'))
      #  CONFIRMAR_NOME = str(input('Confirma sua Alteração?')).upper()
       # while CONFIRMAR_NOME == 'NAO' or CONFIRMAR_NOME == 'NÃO':
        #    NOME = str(input('Digite Seu Nome:'))
         #   CONFIRMAR_NOME = str(input('Confirma sua Alteração?')).upper()
       # if CONFIRMAR_NOME == 'SIM':
        #    ENDERECO = str(input('Digite Seu endereço:'))
         #   NUMERO_ENDERECO = int(input('Digite o numero do endereço:'))
          #  CONFIRMAR_ENDERECO = str(input('Confirma o seu Endereço e numero?')).upper()
           # while CONFIRMAR_ENDERECO == 'NAO' or CONFIRMAR_NOME == 'NÃO':
            #    ENDERECO = str(input('Digite Seu endereço:'))
             #   NUMERO_ENDERECO = int(input('Digite o numero da sua casa'))
              #  CONFIRMAR_ENDERECO = str(input('Confirma o seu Endereço e numero?')).upper()
               # if CONFIRMAR_ENDERECO == 'SIM':
                #    print('Dados confirmados!')

    CPF = input('Digite seu CPF (somente números): ')
    while not (CPF.isdigit() and len(CPF) == 11):
        print('CPF Inválido, tente novamente')
        CPF = input('Digite seu CPF (somente números): ')
    else:
        NOME = str(input('Digite Seu Nome:'))
        CONFIRMAR_NOME = str(input('Confirma sua Alteração?')).upper()
        while CONFIRMAR_NOME == 'NAO' or CONFIRMAR_NOME == 'NÃO':
            NOME = str(input('Digite Seu Nome:'))
            CONFIRMAR_NOME = str(input('Confirma sua Alteração?')).upper()
        if CONFIRMAR_NOME == 'SIM':
            ENDERECO = str(input('Digite Seu endereço:'))
            NUMERO_ENDERECO = int(input('Digite o numero do endereço:'))
            CONFIRMAR_ENDERECO = str(input('Confirma o seu Endereço e numero?')).upper()
            while CONFIRMAR_ENDERECO == 'NAO' or CONFIRMAR_NOME == 'NÃO':
                ENDERECO = str(input('Digite Seu endereço:'))
                NUMERO_ENDERECO = int(input('Digite o numero da sua casa'))
                CONFIRMAR_ENDERECO = str(input('Confirma o seu Endereço e numero?')).upper()
                if CONFIRMAR_ENDERECO == 'SIM':
                    print('Dados confirmados, sua alteração foi realizada!')
                    TELEFONE = input('DIGITE SEU TELEFONE COM DDD (somente números): ')
                    CONFIRMAR_TELEFONE = str(input('CONFIRMA O NUMERO DE TELEFONE DIGITADO?'))
                    while not (TELEFONE.isdigit() and len(TELEFONE) == 11):
                        print('TELEFONE Inválido, tente novamente')
                        TELEFONE = input('Digite seu TELEFONE COM DDD (somente números): ')
                    else:
                        print('NÚMERO DE TELEFONE CONFIRMADO')
                        print('ESCOLHA SEU PROVEDOR DE E-MAIL')
                        print('[1] gmail.com')
                        print('[2] hotmail.com')
                        print('[3] yahoo.com.br')
                        PROVEDOR_1 = "gmail.com"
                        PRVEDOR_2 = "hotmail.com"
                        PRVEDOR_3 = "yahoo.com.br"

                        PROVEDOR_EMAIL = int(input('DIGITE O NÚMERO DO SEU PROVEDOR: '))

                        email = input('DIGITE SEU EMAIL: ')
                        CONFIRMAR_EMAIL = input('CONFIRMA O E-MAIL DIGITADO? ').upper()

                        while CONFIRMAR_EMAIL in ('NAO', 'NÃO'):
                            email = input('DIGITE SEU E-MAIL: ')
                            CONFIRMAR_EMAIL = input('CONFIRMA O E-MAIL DIGITADO? ').upper()
                        if CONFIRMAR_EMAIL == 'SIM' :
                            print('Os dados a seguir foram alterados:')
                            print('{}'.format(NOME))
                            print('{}'.format(ENDERECO))
                            print('{}'.format(TELEFONE))
                            print('{}{}'.format(email,PROVEDOR_EMAIL))


elif usuario == 'GERENTE':
    senha = int(input('Digite sua Senha Corporativa:'))
    if senha != 302010:
        print('Senha Inválida')
    elif senha == 302010:
            print('Seja Bem-Vindo Gerente !!')
            print('[1] GERAR RELATÓRIOS DE PEDIDOS')
            print('[2] GERAR RELATÓRIOS DE ENTREGAS')
            print('[3] GERAR RELATÓRIOS DE CARGAS')
            print('[4] GERAR RELATÓRIOS DE VEÍCULOS')
            print('[5] GERAR RELATÓRIO FINANCEIRO')
            print('[6] GERAR RELATÓRIOS DE ESTOQUE')
            print('[7] GERAR RELATÓRIOS DE ENTREGAS REALIZADAS')
            print('[8] GERAR RELATÓRIOS DE ENTREGAS PENDENTES')
            print('[9] GERAR RELATÓRIOS DE ENTREGAS ATRASADAS')
            print('[10] GERAR RELATÓRIOS DE DESPESAS')
            print('[11] GERAR RELATÓRIOS DE RECEITAS')
            print('[12] EXIBIR CUSTOS DE MANUTENÇÃO')
            FUNCAO = str(input('DIGITE O NUMERO DO RELATÓRIO QUE DESEJA:'))


#VITOR ADICIONE BANCO DE DADOS PARA GERAR RELATORIOS BASEADO NOS DADOS SOLICITADOS, VOCÊ SÓ VAI COLOCAR A INSTRUÇAO

elif usuario == 'FUNCIONARIO' or 'FUNCIONÁRIO':
    SENHA_FUNCIONARIO = int(input('DIGITE SUA SENHA CORPORATIVA'))
    if SENHA_FUNCIONARIO == '301020':
        print('[0] REGISTRAR PONTO')
        print('[1] CONSULTAR DADOS CADASTRAIS')
        print('[2] CONSULTAR PEDIDOS EM TRANSPORTE')
        print('[3] CONSULTAR INFORMAÇÕES DE CARGA')
        print('[4] REGISTRAR COLETA')
        print('[5] REGISTRAR ENTREGA')
        print('[6] ALTERAR O STATUS DO PEDIDO CONFORME A ATIVIDADE REALIZADA')
        print('[7] REGISTRAR INFORMAÇÕES RELACIONADAS Á COLETA')
        print('[8] REGISTRAR INFORMAÇÕES RELACIONADAS Á ENTREGA')
        print('[9] CONSULTAR ENDEREÇO DE ENTREGA')
        print('[10] CONSULTAR ENDEREÇO DE COLETA')
        print('[11] CONSULTAR INFORMAÇÕES DO CLIENTE')
        print('[12] REGISTRAR MOVIMENTAÇÃO DE CARGA NO ARMAZÉM')
        print('[13] CONSULTAR CARGAS ARMAZENADAS')
        print('[14] CONSULTAR VEÍCULO E MOTORISTA ASSOCIADO A CARGA')
        print('[15] REGISTRAR/ CONSULTAR OCORRENCIA DE TRANSPORTE')
        print('[16] CONSULTAR HISTÓRICO DE OPERAÇÕES DIÁRIAS')
#VITOR ADICIONE BANCO DE DADOS PARA GERAR RELATORIOS BASEADO NOS DADOS SOLICITADOS, VOCÊ SÓ VAI COLOCAR A INSTRUÇAO

#if usuario == 'ADMIN' or 'ADMINISTRADOR':


elif usuario == 'FUNDADOR' or 'DONO' or 'PROPRIETARIO' or 'PROPRIETÁRIO':
    SENHA_PROPRIETARIO = int(input('DIGITE SUA SENHA CORPORATIVA: '))
    if SENHA_PROPRIETARIO == 301020:
        print('COMO POSSO AJUDA-LO HOJE?')
        print('[0] CONSULTAR DADOS DA EMPRESA')
        print('[1] ALTERAR DADOS DA EMPRESA')
        print('[2] CADASTRAR CLIENTE')
        print('[3] ALTERAR DADOS DO CLIENTE')
        print('[4] INATIVAR CLIENTE')
        print('[5] CONSULTAR CLIENTES')
        print('[6] CONSULTAR PEDIDOS DE TRANSPORTE')
        print('[7] CONSULTAR HISTÓRICO DE PEDIDOS')
        print('[8] CONSULTAR CARGAS EM TRANSPORTE')
        print('[9] CONSULTAR CARGAS ARMAZENADAS')
        print('[10] CONSULTAR VEÍCULOS')
        print('[11] CONSULTAR MOTORISTAS')
        print('[12] CONSULTAR DISPONIBILIDADE DOS VEÍCULOS')
        print('[13] CONSULTAR HISTÓRICO DE MANUTENÇÃO')
        print('[14] CONSULTAR RECEITAS E DESPESAS')
        print('[15] CONSULTAR PAGAMENTOS PENDENTES')
        print('[16] CONSULTAR FLUXO FINANCEIRO')
        print('[17] GERAR RELATÓRIO FINANCEIRO')
        print('[18] GERAR RELATÓRIO DE PEDIDOS')
        print('[19] GERAR RELATÓRIO DE ENTREGAS')
        print('[20] GERAR RELATÓRIO DE CARGAS')
        print('[21] GERAR RELATÓRIO DE VEÍCULOS')
        print('[22] GERAR RELATÓRIO DE ESTOQUE')
        print('[23] CONSULTAR ENTREGAS REALIZADAS')
        print('[24] CONSULTAR ENTREGAS PENDENTES')
        print('[25] CONSULTAR ENTREGAS ATRASADAS')
        print('[26] CONSULTAR HISTÓRICO DE OPERAÇÕES DOS FUNCIONÁRIOS')
        print('[27] ACOMPANHAR TRANSPORTES EM ANDAMENTO')
        print('[28] CONSULTAR INDICADORES DA EMPRESA')
    else:
        print('SENHA INCORRETA')
else:
    print('Você Digitou algo errado,refaça a operação')