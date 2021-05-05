import os
import pandas as pd



def cad_fis(cad_fis):
        cad_fis = nome, endereço, bairro, numero, cidade, estado, complemento, telefone, email, cpf
        arquivo = open('cadastrofisico.csv', 'a')
        dados = list()
        dados.append(cad_fis)
        arquivo.writelines(str(dados))
        arquivo.writelines('\n')
        arquivo.close()
        return print('Dados cadastrados: ', cad_fis)




def cad_jur(cad_jur):
        cad_jur = nome_emp, endereço, bairro, numero, cidade, estado, complemento, telefone, email, cnpj
        arquivo = open('cadastrojuridico.csv', 'a')
        dados = list()
        dados.append(cad_jur)
        arquivo.writelines(str(dados))
        arquivo.writelines('\n')
        arquivo.close()
        return print('Dados da empresa cadastrada: ', cad_jur)




def cad_prod(cad_prod):
        cad_prod = nome_prod, codigo, quantidade, preco
        arquivo = open('cadastroproduto.csv', 'a')
        dados = list()
        dados.append(cad_prod)
        arquivo.writelines(str(dados))
        arquivo.writelines('\n')
        arquivo.close()
        return print('Produto: ', cad_prod)



def pesqfis(pesqfis):
         return print(pd.read_csv('cadastrofisico.csv', sep =';', header=None))


def pesqjur(pesqjur):
        return print(pd.read_csv('cadastrojuridico.csv', sep=' ', header=None))


def pesqprod(pesqprod):
        return print(pd.read_csv('cadastroproduto.csv', sep=' ', header=None))





menu = input('Selecione a opção desejada:\n'
             '1- Cadastro de pessoa física\n'
             '2- Cadastro de pessoa jurídica\n'
             '3- Cadastro de produto\n'
             '4- Busca pessoa física\n'
             '5- Busca pessoa jurídica\n'
             '6- Busca produto\n'
             '0- Sair\n'
             'Opção:')

while menu > '0':

        if menu == '1':
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
                cad_fis(cad_fis)
                s= input('Deseja cadastrar novamente? (digite S ou N para menu):')
                if s == 'S':
                        continue
                else:
                        break



        elif menu == '2':
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
                cad_jur(cad_jur)
                s = input('Deseja cadastrar novamente? (digite S ou N para menu):')
                if s == 'S':
                        continue
                else:
                        break


        elif menu == '3':
                nome_prod = input('Nome do produto: ')
                codigo = input('Código do produto:  ')
                quantidade = input('Quantidade:  ')
                preco = input('Preço: ')
                cad_prod(cad_prod)
                s = input('Deseja cadastrar novamente? (digite S ou N para menu):')
                if s == 'S':
                        continue
                else:
                        break



        elif menu == '4':
                    pesqfis(pesqfis)
                    break

        elif menu == '5':
                pesqjur(pesqjur)
                break

        elif menu == '6':
             pesqprod(pesqprod)
             break



















