import json 

#CADASTRANDO USUÁRIOS

def cadastro(): 
    itens_cadastro= []
    with open('database.json', 'r',  encoding='utf-8') as trans: # convertendo json para python 
        itens_cadastro= json.load(trans)
    
    nome = input('Digite um nome: ').strip()
    id_cartao= input('Digite o id do cartão: ').strip()
   
    # Caso o id já esteja cadastrado, ele não deixa cadastrar o mesmo id
    for p  in range(len(itens_cadastro)) :
        if itens_cadastro[p]['id_cartao'] == id_cartao: 
            print('ID já cadastrado no sistema') 
            break
    else: 
        cargo = input('Digite o cargo: ').strip()
        permissao_menu= print('''PERMISSÃO 
        1- Permitido 
        2- Negado''') # mostrando as opções para a variavel permissão
        permissao= ''
        while permissao != '1' and permissao != '2': # conferindo se o usuário tem permissão ou não 
            permissao = input('Digite permissão: ')
            
            if permissao == '1': 
                print('Permitido')
            
            elif permissao == '2': 
                print('Negado')
        
    
      
        itens_cadastro.append(dict(nome = nome, id_cartao = id_cartao,  cargo= cargo, permissao = 'Permitido' if permissao == '1' else 'Negada')) # adicionando os dados cadastrados na lista

        
    with open('database.json', 'w',  encoding='utf-8' ) as trans: # convertendo python para json 
         json.dump(itens_cadastro, trans, indent= '\t', ensure_ascii=False) 


cadastro()
    