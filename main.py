from entities.facts import facts
from entities.schema import schema
from service.facts_service import get_current_facts


def main():
    # Obtém os fatos vigentes usando o serviço
    current_facts = get_current_facts(facts, schema)

    # Exibe os fatos vigentes
    for fact in current_facts:
        print(fact)


if __name__ == "__main__":
    main()
