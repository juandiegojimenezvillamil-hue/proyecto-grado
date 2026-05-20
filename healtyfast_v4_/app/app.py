from flask import Flask
from routes.routes import main_routes

app = Flask(__name__)

# Clave secreta para sesiones
app.secret_key = 'healthyfast_arquitectura_segura_2026'

# Registrar Blueprint principal
app.register_blueprint(main_routes)

# Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)
