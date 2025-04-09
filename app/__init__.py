from flask import Flask
import os

app = Flask(__name__, template_folder=os.path.join('views', 'templates'),
            static_folder=os.path.join('views', 'static'),
            static_url_path='/static')

# Importa aquí los controladores (blueprints) después de crear la instancia de la app
from app.controllers import home_controller, contact_controller

# Registra los blueprints
app.register_blueprint(home_controller.bp)
app.register_blueprint(contact_controller.bp)