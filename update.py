#Update

import json 

def alterar_nome():
    with open('database.json' , 'r') as trans: 
        itens_cadastro = json.load(trans) 

    id_cartao_visualizar= input('Digite o id a ser atualizado: ').strip()


    # Novas informações do usuário
    novo_nome= input('Digite nome atualizado: ').strip()
    novo_id= input('Digite o novo id do cartão: ').strip()
    novo_cargo= input('Digite o novo cargo: ').strip()
    permissao_menu= print('''PERMISSÃO 
    1- Permitido 
    2- Negado''')
    permissao_nova = input('Digite permissão: ')
        
    if permissao_nova == '1': 
        print('Permitido')
        
    elif permissao_nova == '2': 
        print('Negado')
    
  
    for p in range(len(itens_cadastro)) :
        #Adcionando as novas informações
        if itens_cadastro[p]['id_cartao'] == id_cartao_visualizar:
            itens_cadastro[p]['nome'] = novo_nome if novo_nome != '' else itens_cadastro[p]['nome']
            itens_cadastro[p]['id_cartao'] = novo_id if novo_id != '' else itens_cadastro[p]['id_cartao']
            itens_cadastro[p]['cargo'] = novo_cargo if novo_cargo != '' else itens_cadastro[p]['cargo']
            itens_cadastro[p]['permissao'] =  'Permitida' if permissao_nova == '1' else 'Negada' if permissao_nova != '' else itens_cadastro[p]['permissao']
    
    else: 
        print('ID não cadastrado!')
            
            
    
        
    with open('database.json', 'w') as trans: 
        json.dump(itens_cadastro, trans, indent='\t',ensure_ascii=False)
    
        
alterar_nome()
