from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
def index():
    titulo = "paguina de Inicio"
    listado = ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route('/calculos')
def calculo():
    return render_template('calculos.html')

@app.route('/distancia')
def distancia():
    return render_template('distancia.html')

@app.route('/hola')
def about():
    return"hola"

@app.route('/user/string:user>')
def user(user):
    return f"hello, {user}!"

@app.route('/numero/<int:num>')
def func(num):
    return f"el, numero es: {num}"

@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    return f"la suma es: {num1 + num2}"

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID: {} nombre: {}".format(id,username)

@app.route('/suma/<float:n1>/<float:n2>')
def func1(n1,n2):
    return "lasuma es: {}".format(n1+n2)

@app.route('/default/')
@app.route('/default/<string:dft>')
def func2(dft= "sss"):
    return "el valor de dft es:"+ dft

@app.route("/prueba")
def func4():
    return '''
    <html>
        <head>
            <title>paguina de prueba<title/>
        </head>
        <body>
            <h1>hola este es una paguina de prueba<h1/>
            <p>esta es la paguina es para probar el retorno dl<p/>
        </body
    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True)