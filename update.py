#Update

import json 

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
                
            while permissao_nova not in ('1','2',' '):
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
        
        
    
 
        
alterar_nome()
