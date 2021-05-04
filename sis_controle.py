import os


def cad_fis(cad_fis):
        cad_fis = nome, endereço, bairro, numero, cidade, estado, complemento, telefone, email, cpf
        arquivo = open('cadastrofisico.txt', 'a')
        dados = list()
        dados.append(cad_fis)
        arquivo.writelines(str(dados))
        arquivo.close()
        return print('Dados cadastrados: ', cad_fis)




def cad_jur(cad_jur):
        cad_jur = nome_emp, endereço, bairro, numero, cidade, estado, complemento, telefone, email, cnpj
        arquivo = open('cadastrojuridico.txt', 'a')
        dados = list()
        dados.append(cad_jur)
        arquivo.writelines(str(dados))
        return print('Dados da empresa cadastrada: ', cad_jur)




def cad_prod(cad_prod):
        cad_prod = nome_prod, codigo, quantidade, preco
        arquivo = open('cadastroproduto.txt', 'a')
        dados = list()
        dados.append(cad_prod)
        arquivo.writelines(str(dados))
        return print('Produto: ', cad_prod)




menu = input('Selecione a opção desejada:\n1- Cadastro de pessoa física\n2- Cadastro de pessoa jurídica\n3- Cadastro de produto\n4- Sair\nOpção:')

if menu < '2':
        nome = input('Nome e sobrenome: ')
        endereço = input('Endereço: ')
        bairro = input('Bairro: ')
        numero = int(input('Número: '))
        cidade = input('Cidade: ')
        estado = input('Estado: ')
        complemento = input('Complemento: ')
        telefone = input('Telefone: ')
        email = input('Email:')
        cpf = input('CPF: ')

elif menu < '3':
        nome_emp = input('Nome da Empresa: ')
        endereço = input('Rua: ')
        bairro = input('Bairro: ')
        numero = input('Número:')
        cidade = input('Cidade: ')
        estado = input('Estado: ')
        complemento = input('Complemento: ')
        telefone = input('Telefone: ')
        email = input('Email: ')
        cnpj = input('CNPJ: ')

elif menu < '4':
        nome_prod = input('Nome do produto: ')
        codigo = input('Código do produto:  ')
        quantidade = input('Quantidade:  ')
        preco = input('Preço: ')

if menu == '1':
        cad_fis(cad_fis)
elif menu == '2':
        cad_jur(cad_jur)
elif menu == '3':
        cad_prod(cad_prod)
elif menu == '4':
        os.system('cls')




