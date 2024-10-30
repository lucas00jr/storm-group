# Inicializa a lista de esquemas como vazia
schema = []


# Função para adicionar um esquema
def add_schema(attribute, cardinality):
    schema.append((attribute, 'cardinality', cardinality))


# Exemplo de como adicionar esquemas iniciais
add_schema('endereço', 'one')
add_schema('telefone', 'many')
