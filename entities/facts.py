# Lista de fatos conhecidos, representando E, A, V e status de adição.
# Inicializa a lista de fatos como vazia
facts = []


# Função para adicionar um fato
def add_fact(entity, attribute, value, added):
    facts.append((entity, attribute, value, added))


# Exemplo de como adicionar fatos iniciais
add_fact('gabriel', 'endereço', 'av rio branco, 109', True)
add_fact('joão', 'endereço', 'rua alice, 10', True)
add_fact('joão', 'endereço', 'rua bob, 78', False)
add_fact('joão', 'endereço', 'rua bob, 88', True)
add_fact('joão', 'telefone', '234-5678', True)
add_fact('joão', 'telefone', '91234-5555', True)
add_fact('gabriel', 'telefone', '98888-1111', True)
add_fact('gabriel', 'telefone', '98888-2222', False)
add_fact('gabriel', 'telefone', '56789-1010', True)
