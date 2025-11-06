from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', titulo="Inicio")

@app.route('/Lugares')
def lugares():
    return render_template('Lugares.html', titulo="Lugares")

@app.route('/Hoteles')
def hoteles():
    return render_template('Hoteles.html', titulo="Hoteles")

@app.route('/Restaurantes')
def restaurantes():
    return render_template('Restaurantes.html', titulo="Restaurantes")

if __name__ == '__main__':
    app.run(debug=True)
