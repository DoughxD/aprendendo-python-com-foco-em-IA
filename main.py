"""
🔮 Missão 2 – Sistema de Despensa Alquímica 🔮

Objetivo:
Criar um sistema modular onde o alquimista pode:
- Adicionar ingredientes à despensa
- Usar ingredientes na preparação de poções
- Visualizar o estoque atual
- Impedir o uso de ingredientes se não houver quantidade suficiente

Requisitos:
1. Função `adicionar_ingrediente(nome, quantidade)`
   - Soma a quantidade se o ingrediente já existir
   - Adiciona ao estoque e à lista `novos_itens` se for novo

2. Função `usar_ingrediente(nome, quantidade)`
   - Verifica se há quantidade suficiente antes de remover
   - Exibe aviso se faltar

3. Função `mostrar_despensa()`
   - Mostra o estoque ordenado por quantidade (maior → menor)
   - Itens adicionados recentemente aparecem destacados em verde (ANSI)

4. Função `limpar_novos_itens()`
   - Limpa a lista `novos_itens`

Regras:
- Usar dicionário global chamado `estoque`
- Usar lista global chamada `novos_itens`
- Só `mostrar_despensa()` pode exibir informações no terminal
- Código modularizado, limpo e comentado

Pontuação (XP):
+1 - Função adicionar_ingrediente()
+1 - Função usar_ingrediente()
+2 - Função mostrar_despensa() com destaque de novos
+1 - Organização e boas práticas

Total máximo: 5 XP

Autor: Douglas Sampaio
"""


import pprint

estoque = {
    "erva_lunar": 5,
    "po_magico": 3,
    "raiz_sagrada": 8,
    "agua_eterea": 10,
    "sal_nigredo": 2,
    "cinzas_de_fenix": 1,
    "pedra_alquimica": 4,
    "sangue_de_dragao": 2,
    "lagrimas_de_sereia": 6,
    "essencia_da_noite": 3,
    "nectar_dos_deuses": 7,
    "musgo_ancestral": 9,
    "fumaça_das_sombras": 2,
    "cristal_solido": 5,
    "raio_congelado": 3,
    "areia_do_tempo": 6,
    "mel_de_lunaris": 4,
    "brasa_viva": 2,
    "pó_de_estrela": 5,
    "gelo_eterno": 1
}
novos_itens = {}

def adicionar_ingrediente(nome, quantidade):
    global estoque
    global novos_itens
    if nome in estoque:
        estoque[nome] += int(quantidade)
        print (f'{estoque[nome]} recebeu {quantidade}')
        print (estoque)
    else:
        estoque[nome] = quantidade
        novos_itens[nome] = quantidade
        print (f'{quantidade} de {nome} foi adicionado ao estoque ')
        print (estoque)
        print (f"\033[92m{novos_itens}\033[0m")

def usar_ingrediente(nome, quantidade):
    if nome in estoque:
        estoque[nome] -= int(quantidade)
        print (f'você usou {quantidade} de {estoque[nome]}')
        print (estoque)
    else:
        print (f"\033[91m Você não tem esse item \033[0m")
    
def mostrar_despensa():
    global estoque
    while True:
        escolha = input("MENU\n"
        "1- Checar estoque \n"
        "2- Ordenar estoque \n"
        "0- voltar  \n"
        "-> ")
        if escolha == '1':
            for nome, quantidade in estoque.items():
                if quantidade > 10:
                    print(f'{nome} \033[91m[{quantidade}]\033[0m')
            for nome, quantidade in estoque.items():
                if quantidade >= 3:
                    print(f'Quantidade de {nome} esta baixa sugiro reposição')
        elif escolha == '2':
            usar_ingrediente(input('nome do ingrediente: '), int(input('quantidade do ingrediente: ')))
        else:
            menu()
       
        

def remover_ingrediente(nome):
    print('remover ingrediente aidna em construção')
    
def menu():
    while True:
        escolha = input("MENU\n"
        "1- Adicionar Ingrediente \n"
        "2- Usar Ingredientes \n"
        "3- Mostrar Dispensa  \n"
        "4- Remover Ingrediente  \n"
        "0- sair  \n"
        "-> ")
        if escolha == '1':
            adicionar_ingrediente(input('nome do ingrediente: '), int(input('quantidade do ingrediente: ')))
        elif escolha == '2':
            usar_ingrediente(input('nome do ingrediente: '), int(input('quantidade do ingrediente: ')))
        elif escolha == '3':
            mostrar_despensa()
        elif escolha == '4':
            remover_ingrediente(input('nome do ingrediente: '),)
        elif escolha == 'sair':
            print('fechando o programa')
            exit()
        else: 
            print('\033[91m esse comando não existe... \033[0m')

if __name__ == "__main__":
    mostrar_despensa()
    'menu()'
        
                    