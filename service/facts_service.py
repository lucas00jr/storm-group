def get_current_facts(facts, schema):
    # Dicionário para armazenar a cardinalidade dos atributos
    cardinality = {attr: card for attr, _, card in schema}

    # Dicionário para armazenar os fatos vigentes
    current_facts = {}

    for entity, attr, value, added in facts:
        # Determinar a chave da entidade-atributo para acessar o fato correto
        key = (entity, attr)

        # Verificar a cardinalidade do atributo
        if cardinality.get(attr) == 'one':
            # Se é one-to-one, armazenamos apenas o fato mais recente
            if added:
                current_facts[key] = (entity, attr, value, True)
            elif key in current_facts:
                # Se houver uma retração (added=False), remove o fato vigente
                del current_facts[key]

        elif cardinality.get(attr) == 'many':
            # Se é one-to-many, armazenamos uma lista de valores vigentes
            if key not in current_facts:
                current_facts[key] = []

            if added:
                # Adiciona o valor atual
                current_facts[key].append((entity, attr, value, True))
            else:
                # Remove qualquer valor correspondente que tenha sido retraído
                current_facts[key] = [fact for fact in current_facts[key] if fact[2] != value]

    result = []
    for key, facts in current_facts.items():
        # Verificar se 'facts' é uma lista (cardinalidade 'many') ou uma única tupla (cardinalidade 'one')
        if isinstance(facts, list):
            result.extend(facts)
        else:
            result.append(facts)

    return result
