from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start-pokemon')
def start_pokemon():
    # Ejecutar el script .pyw usando subprocess
    subprocess.Popen(['pythonw', 'pokemon_app.pyw'])
    return "Script ejecutado"

if __name__ == '__main__':
    app.run(debug=True)
