from flask import Flask, render_template, request
import forms

app = Flask(__name__)

@app.route('/index')
def index():
    titulo = "paguina de Inicio"
    listado = ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS']
    return render_template('index.html', titulo=titulo, listado=listado)

@app.route('/calculos',methods=['GET','POST'])
def calculo():
    if request.method == 'POST':
        numero1 = request.form['numero1']
        numero2 = request.form['numero2']
        opcin = request.form['operacion']
        if opcin == 'suma':
            res = int(numero1) + int(numero2)
        if opcin == 'resta':
            res = int(numero1) - int(numero2)
        if opcin == 'multiplicacion':
            res = int(numero1) * int(numero2)
        if opcin == 'division':
            res = int(numero1) / int(numero2)
        return render_template('calculos.html', res=res, numero1=numero1, numero2=numero2)

    return render_template('calculos.html')

@app.route('/distancia',methods=['GET','POST'])
def distancia():
    if request.method == 'POST':
        distanciax1 = request.form['distanciax1']
        distanciay1 = request.form['distanciay1']
        distanciax2 = request.form['distanciax2']
        distanciay2 = request.form['distanciay2']
        opcione = request.form['operaci']
        if opcin == 'distanciaa':
            dist = Math.sqrt((int(distanciax2) - int(distanciax1)) * (int(distanciax2) - int(distanciax1)) +  (int(distanciay2) - int(distanciay1)) * (int(distanciay2) - int(distanciay1)))
        return render_template('calculos.html', dist=dist, distanciax1=distanciax1, distanciay1=distanciay1, distanciax2=distanciax2, distanciay2=distanciay2)
        
    return render_template('distancia.html')

@app.route("/Alumnos",methods=['GET','POST'] )
def alumnos():
    mat=0
    nom=""
    ape=""
    email=""
    alumno_clas=forms.UserForm(request.form)
    if request.method == 'POST' and alumno_clas.validate():
        mat=alumno_clas.matricula.data
        nom=alumno_clas.nombre.data
        ape=alumno_clas.apellido.data
        email=alumno_clas.correo.data
    
    return render_template('Alumnos.html', form=alumno_clas, mat=mat,nom=nom,ape=ape,email=email)

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