import json 

#EXCLUIR USUÁRIO

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
