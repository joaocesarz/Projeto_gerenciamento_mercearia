# é simplesmente uma função Python que recebe uma requisição Web e retorna uma resposta Web.

from controller import CategoriaController, ProdutosController, FornecedorController
from dao import CategoriaDao, ProdutosDao, FornecedorDao

print('======================= Gerenciamento de Mercearia =======================')
print()
print()



while True:
    decisao2 = input('[1]Categoria [2]Produto [3]Fornecedor [4]Cliente [5]Funcionário [0]Fechar: ')
    decisao2 = int(decisao2)

    print('')
    if decisao2 == 0:
        break



# Área de Cadastro/Alteração/Remoção

    if decisao2 == 1:
        categoria = input('[C]adastrar [A]lterar [R]emover [V]oltar: ').lower()

        if categoria == 'c':
            mostrar = CategoriaDao.lercategoria()
            for i in mostrar:
                print(i, end='')
            nome_categoria = input('Nome da categoria: ').upper()
            CategoriaController.cadastrarCategoria(nome_categoria)  # Chamando controller      

        elif categoria == 'a':
            x = CategoriaDao.lercategoria()
            for i in x:
                print(i, end='')
            alterar_categoria = input('Digite o nome da categoria que deseja alterar: ').upper()
            alterada_categoria = input('Digite o nome da nova categoria alterada: ').upper()
            CategoriaController.alterarCategoria(alterarCategoria=alterar_categoria, alteradaCategoria=alterada_categoria)

        elif categoria == 'r':
            x = CategoriaDao.lercategoria()
            for i in x:
                print(i, end="")
    
            indice_categoria = input('Digite o nome da categoria que dejesa remover: ').upper()

            CategoriaController.removerCategoria(indice_categoria)

        elif categoria == 'v':
            continue
    
        else:
            print('')
            print('Desculpe.. Opção inválida. Tente novamente.')
            print('Opções [C] [R] [A] [V]')
            print('')
            continue



# Área de Produtos

    elif decisao2 == 2:
        produtos = input('[C]adastrar [A]lterar [R]emover [V]oltar: ').lower()

        if produtos == 'c':
            nome = input('Nome do produto: ').upper()
            preco = input('Valor do produto: R$')
            categoria = input('Categoria do produto: ').upper()
            ProdutosController.cadastrarProduto(nome=nome, preco=preco, categoria=categoria)
   
        elif produtos == 'a':
            # mostrar = Produtos.lerProdutos()
            # for i in mostrar:
            #    print(i, end='')
            
            nome_alterar = input('Nome do produto que deseja alterar: ').upper()
            nome_alterado = input('Nome do produto: ').upper()
            valor_alterado = input('Valor do produto: R$').upper()
            categoria_alterada = input('Categoria do produto: ').upper()
            ProdutosController.alterarProduto(alterarProduto=nome_alterar, nome=nome_alterado, 
            preco=valor_alterado, categoria=categoria_alterada)

        elif produtos == 'r':
            mostrar = ProdutosDao.lerProduto()
            for i in mostrar:
                print(i, end='')

            produtoRemovido = input('Digite nome do produto que deseja remover: ').upper()
            ProdutosController.removerProduto(nomeProduto=produtoRemovido)

        elif produtos == 'v':
            continue

        else:
            print('')
            print('Desculpe... Opção inválida. Tente novamente.')
            print('Opções [C] [R] [A] [V]')
            print('')
            continue

    
    elif decisao2 == 3:
        fornecedor = input('[C]adastrar [A]lterar [R]emover [V]oltar: ').lower()

        if fornecedor == 'c':
            
            nomeForne = input('Nome do fornecedor: ').upper()
            telefone = input('Número de telefone: ')
            cnpj = input('Digite CNPJ da empresa: ')
            categoria = input('DIgite a categoria: ').upper()

            FornecedorController.cadastrar(nome=nomeForne, telefone=telefone, cnpj=cnpj, categoria=categoria)

        elif fornecedor == 'r':
            
            removerFornecedor = input('Nome do fornecedor: ').upper()
            FornecedorController.removerFornecedor(nomeFornecedor=removerFornecedor)
        
        elif fornecedor == 'a':
            mostrar = FornecedorDao.ler_fornecedores()
            for i in mostrar:
                print(i, end=(''))

            alterar = input('Nome do fornecedor: ').upper()
            print('Informações da alteração do fornecedor')
            nomeAlt = input('Nome do fornecedor: ').upper()
            telAlt = input('Digite o telefone: ')
            cnpjAlt = input('Digite o cnpj: ')
            catAlt = input('Digite a categoria: ').upper()

            FornecedorController.alterarFornecedor(alterarForne=alterar,nome=nomeAlt,
            telefone=telAlt, cnpj=cnpjAlt, categoria=catAlt)

        elif fornecedor == 'v':
            continue

        else:
            print('')
            print('Desculpe... Opção inválida, tente novamente as opções...')
            print('Digite [C] [R] [A] [V]')
            print('')
            continue

    elif decisao2 == 4:
        cliente = input('[C]adastrar [A]lterar [R]emover: ').lower()

        if cliente == 'c':
            nomeClt = input('Nome do cliente: ').upper()
            cpfClt = input('Digite o CPF: ').upper()
            emailClt = input('Digite seu Email: ').lower()
            telefoneClt = input('Telefone de contato: ')
            enderecoclt = input('Digite seu endereço: ').upper()

        elif cliente == 'r':
            ...

        elif cliente == 'a':
            ...

        else:
            print('Desculpe, não consegui fazer sua solicitação')

    elif decisao2 == 5:
        funcionario = input('[C]adastrar [A]lterar [R]emover: ').lower()

        if funcionario == 'c':
            ...
# Tratamento


    else:
        print('Desculpe... Opção desejava inválida. Por favor...')
        print('Tente novamente')
        print('Opção abaixo.')
        print('')
        continue
