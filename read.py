import json 

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
