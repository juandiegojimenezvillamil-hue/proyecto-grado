from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/')
@app.route('/menu')

def Menu():
    return render_template('/pages/menu.html')

@app.route('/inventario')
def Inventario():
    return render_template('/pages/inventario.html')

@app.route('/productos')
def Productos():
    return render_template('/pages/productos.html')



if __name__ == '__main__':
    app.run(debug=True)