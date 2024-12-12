from flask import Flask
from rutas.rutas_miembros import bp_miembros
from rutas.rutas_entrenadores import bp_entrenadores
from rutas.rutas_clases import bp_clases
from rutas.rutas_inscripciones import bp_inscripciones

app = Flask(__name__)

app.register_blueprint(bp_miembros)
app.register_blueprint(bp_entrenadores)
app.register_blueprint(bp_clases)
app.register_blueprint(bp_inscripciones)

if __name__ == "__main__":
    app.run(debug=True)
