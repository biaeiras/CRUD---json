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


#cadastro()
    
    


# VISUALIZAR OS USUÁRIOS

# Vendo todos os usuários cadastrados 
def visualizar_cadastrados():
    with open('database.json' , 'r') as trans: 
       itens_cadastro = json.load(trans) 
    for pessoas in itens_cadastro: 
         print(pessoas)
       

#visualizar_cadastrados()

# Procurando cadastrados pelo nome
def visualizar_cadastrado_nome():
    with open('database.json' , 'r') as trans: 
        itens_cadastro = json.load(trans) 

    nome_consulta= input(' Digite o nome: ') 
    
    for pessoa in range(len(itens_cadastro)) :
        if itens_cadastro[pessoa]['nome'] == nome_consulta: 
            print(itens_cadastro[pessoa])
            break
        
    else: 
        print('Pessoa não cadastrada no sistema!')
     
#visualizar_cadastrado_nome()


#Procurando cadastro pelo id do cartão
def visualizar_cadastrado_id():
    with open('database.json' , 'r') as trans: 
        itens_cadastro = json.load(trans) 

    id_cartao_visualizar= int(input(' Digite o id: '))
    
    for p  in range(len(itens_cadastro)) :
        if itens_cadastro[p]['id_cartao'] == id_cartao_visualizar: 
            print(itens_cadastro[p])
            break
    else: 
        print('Pessoa não cadastrada no sistema!')

#visualizar_cadastrado_id()


#EXCLUIR USUÁRIO

# Excluindo o usuário pelo nome

# Excluindo o usuário pelo nome
def excluir_cadastro_nome(): 
    with open('database.json' , 'r') as trans: 
        itens_cadastro = json.load(trans) 
    
    deletar_pessoa_nome = input('Digite o nome a ser excluído: ')
    
    for p in range(len(itens_cadastro)) :
        if  itens_cadastro[p]['nome'] ==  deletar_pessoa_nome: 
            itens_cadastro.pop(p)
            print('Usuário deletado com sucesso!')
            break
    
    else: 
        print('Não há pessoas com esse nome')
        
    with open('database.json', 'w') as trans: 
        json.dump(itens_cadastro, trans, indent='\t')
        

excluir_cadastro_nome()

#Excluindo o usuário pelo id do cartão
def excluir_cadastro_id(): 
    with open('database.json' , 'r') as trans: 
        itens_cadastro = json.load(trans) 
    
    excluir_cadastro_id = input('Digite o id a ser excluído: ')
    
    for p in range(len(itens_cadastro)) :
        if  itens_cadastro[p]['id_cartao'] ==  excluir_cadastro_id: 
            itens_cadastro.pop(p)
            print('Usuário deletado com sucesso!')
            break
    
    else: 
        print('Não há id com esse nome')
        
    with open('database.json', 'w') as trans: 
        json.dump(itens_cadastro, trans, indent='\t')
       

#excluir_cadastro_id()

#UPDATE

def alterar_nome():
    with open('database.json' , 'r') as trans: 
        itens_cadastro = json.load(trans) 

    id_cartao_visualizar= input('Digite o id a ser atualizado: ').strip()

    for p in itens_cadastro:
        if p['id_cartao'] == id_cartao_visualizar:
            # Novas informações do usuário
            novo_nome= input('Digite nome atualizado: ').strip()
            novo_id= input('Digite o novo id do cartão: ').strip()
            novo_cargo= input('Digite o novo cargo: ').strip()
            permissao_menu= print('''PERMISSÃO 
            1- Permitido 
            2- Negado''')
            permissao_nova = None
                
            while permissao_nova not in ('1','2',''):
                permissao_nova = input('Digite permissão: ')
                if permissao_nova == '1': 
                    print('Permitido')
                    
                elif permissao_nova == '2': 
                    print('Negado')
                
            for p in itens_cadastro:
                #Adicionando as novas informações
                if p['id_cartao'] == id_cartao_visualizar:
                    p['nome'] = novo_nome if novo_nome != '' else p['nome']
                    p['id_cartao'] = novo_id if novo_id != '' else p['id_cartao']
                    p['cargo'] = novo_cargo if novo_cargo != '' else p['cargo']
                    p['permissao'] =  'Permitida' if permissao_nova == '1' else 'Negada' if permissao_nova != '' else p['permissao']
                    break 
          
                    
            with open('database.json', 'w', encoding='utf-8') as trans: 
                json.dump(itens_cadastro, trans, indent='\t',ensure_ascii=False)
            break
    else: 
        print('Id não cadastrado no sistema!')
        
        
    
 
        
#alterar_nome()

