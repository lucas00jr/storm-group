from flask import Flask, render_template, request, redirect, url_for
from entities.facts import facts
from entities.schema import schema
from service.facts_service import get_current_facts

app = Flask(__name__)


@app.route('/')
def index():
    current_facts = get_current_facts(facts, schema)
    return render_template('index.html', facts=facts, schema=schema, factsFiltrados=current_facts)


@app.route('/add_fact', methods=['GET', 'POST'])
def add_fact():
    if request.method == 'POST':
        entity = request.form['entity']
        attribute = request.form['attribute']
        value = request.form['value']
        added = request.form['added']
        facts.append((entity, attribute, value, added))
        return redirect(url_for('index'))
    return render_template('add_fact.html')


@app.route('/add_schema', methods=['GET', 'POST'])
def add_schema():
    if request.method == 'POST':
        attribute = request.form['attribute']
        cardinality = request.form['cardinality']
        schema.append((attribute, 'cardinality', cardinality))
        return redirect(url_for('index'))
    return render_template('add_schema.html')


if __name__ == '__main__':
    app.run(debug=True)
