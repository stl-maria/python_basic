restaurantes = [{'nome': 'Pão', 'ativo': True}, {'nome': 'Pizza', 'ativo': False}, {'nome': 'Sushi', 'ativo': True}]


for restaurante in restaurantes:  # laço de repetição para acessar todos os elementos na lista de dicionarios
    nome_restaurantes = restaurante['nome']  # acessando os valores
    print(nome_restaurantes)  # saída: Pão Pizza Sushi
    
for restaurante in restaurantes:
    restaurante['tipo'] = 'vegano'  # adiciona um par
    print(restaurante)  # saída: {'nome': 'Pão', 'ativo': True, 'tipo': 'vegano'} {'nome': 'Pizza', 'ativo': False, 'tipo': 'vegano'} {'nome': 'Sushi', 'ativo': True, 'tipo': 'vegano'}
    
for restaurante in restaurantes:
	del restaurante['tipo']  # remove um par
    
	print(restaurante)  # saída: {'nome': 'Pão', 'ativo': True} {'nome': 'Pizza', 'ativo': False} {'nome': 'Sushi', 'ativo': True}
     
for restaurante in restaurantes:
     chaves = restaurante.keys()  # obtendo as chaves 
     valores = restaurante.values()  # obtendo os valores
     print(chaves)  # saída: dict_keys(['nome', 'ativo'])
     print(valores)  # saída: dict_values(['Pão', True])...



