from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/votar', methods=['POST'])
def voto():
    candidato = request.form['candidato']

    with open('votos.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([candidato])
    
    return redirect('/resultados')


@app.route('/resultados')
def resultados():
    with open('votos.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        votos = list(reader)

    candidatos = {}

    for voto in votos:
        candidato = voto[0]
        candidatos[candidato] = candidatos.get(candidato, 0) + 1

    return render_template('resultado.html', candidatos=candidatos)

if __name__ == '__main__':
    app.run(debug=True)
        