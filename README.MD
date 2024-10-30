# Facts Application

## Descrição

Esta é uma aplicação simples para gerenciar e consultar fatos relacionados a entidades e seus atributos. Os dados são representados por tuplas, onde cada tupla contém uma entidade, um atributo, um valor e um indicador de se o fato foi adicionado ou removido.

## Funcionalidades

- **Adicionar Fatos**: Insira novos fatos, especificando entidade, atributo, valor e se está ativo ou não.
- **Adicionar Esquemas**: Configure a cardinalidade (um ou muitos) para cada tipo de atributo.
- **Visualizar Fatos Vigentes**: Veja as informações atuais das entidades, de acordo com a cardinalidade e status de cada fato.

## Pré-requisitos

- Python 3.8 ou superior
- Flask (ver instruções de instalação abaixo)

## Como utilizar

### Clonando o Repositório e Configurando o Ambiente

1. **Clone o repositório**:
   ```bash
   git clone git@github.com:lucas00jr/storm-group.git
   ```
   
2. **Crie e ative o ambiente virtual**:
```bash
  python -m venv venv
      source venv/bin/activate  # Para macOS/Linux
    # ou
      venv\Scripts\activate  # Para Windows
```

3. **Instale as dependências com Poetry e Flask**:
```bash
  curl -sSL https://install.python-poetry.org | python3 -
  
  poetry install
  
  pip install Flask
```
4. **Inicie a aplicação**:
```bash
  poetry run python app.py
```
5. **Acesse a aplicação no navegador**:
   - http://127.0.0.1:5000/

## Estrutura dos Dados

Os dados são representados por "fatos" no formato de tuplas. Cada fato segue a estrutura `(entidade, atributo, valor, ativo?)`, onde o último elemento indica se o fato está ativo (`True`) ou não (`False`).

Exemplo:
```python
facts = [
    ('joão', 'idade', 18, True),
    ('joão', 'telefone', '234-5678', False)
]
```

## Schema de Cardinalidade

Defina a cardinalidade de cada atributo para especificar se ele pode ter múltiplos valores ou apenas um.

Exemplo:
```python
schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]
```

## Executando Testes Unitários

Para executar os testes unitários, utilize o comando:

Exemplo:
```bash
  python -m unittest discover tests/
```


