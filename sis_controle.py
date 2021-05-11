import os
import pandas as pd


def test():
        test = { 'Nome: ' + input('nome:') + ' ' + 'sobrenome:  ' + input('sobrenome: ')}
        arquivo = open('test.csv', 'a')
        arquivo.writelines(test)
        arquivo.close()
        return print(test)






def cad_fis(cad_fis):
        cad_fis = {'Nome: ' + input('Nome: ') + ' ' + 'Sobrenome: ' + input('Sobrenome: ') + ', ' +
                   'Endereço: ' + input('Endereço: ') +  ', ' + 'Número: ' + input('Número: ') + ', ' +'Bairro: ' + input('Bairro: ')
                   + 'Cidade: ' + input('Cidade: ') + ', ' + 'Estado: ' + input('Estado: ') + ', ' + 'Telefone: ' + input('Telefone: ')
                   + ', ' + 'Email: ' + input('Email: ') + ', ' + 'CPF: ' + input('CPF: ')
                   }
        arquivo = open('cadastrofisico.csv', 'a')
        arquivo.writelines(cad_fis)
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
        df= pd.read_csv('cadastrofisico.csv', sep=';', header=None)
        #c= df.rename(columns={'0':'A','1':'b'})
        return print(df)


def pesqjur(pesqjur):
        return print(pd.read_csv('cadastrojuridico.csv', sep=' ', header=None))


def pesqprod(pesqprod):
        df = pd.read_csv('cadastroproduto.csv', sep=';', header=None)
        c = df.rename(columns={0:'Nome produto', 1:'Código', 2:'Quantidade', 3:'Preço'})
        return print(c)




while True:
        print(' ***** PyCads alpha *****\n\n '
              
                        'Selecione a opção desejada:\n'
                        '1- Cadastro de pessoa física\n'
                        '2- Cadastro de pessoa jurídica\n'
                        '3- Cadastro de produto\n'
                        '4- Busca pessoa física\n'
                        '5- Busca pessoa jurídica\n'
                        '6- Busca produto\n'
                        '0- Sair\n')

        menu = input('Opção:')
        if menu == '1':

                cad_fis(cad_fis)
                s = input('Voltar ao menu principal? (digite S ou N para sair):')
                if s == 'S' or 's':
                        continue
                else:
                        s == 'N' or 'n'
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
                s = input('Voltar ao menu principal? (digite S ou N para sair):')
                if s == 'S' or 's':
                       continue
                else:
                       break


        elif menu == '3':
                nome_prod = input('Nome do produto: ')
                codigo = input('Código do produto:  ')
                quantidade = input('Quantidade:  ')
                preco = input('Preço: ')
                cad_prod(cad_prod)
                s = input('Voltar ao menu principal? (digite S ou N para sair):')
                if s == 'S' or 's':
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

        elif menu == '0':
                print('*****Saindo*****')
                break



        elif menu == '7':
                test()
                break




















