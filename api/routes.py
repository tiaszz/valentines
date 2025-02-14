from flask import render_template, jsonify
import os
from api import app

GIF_FOLDER = os.path.join(os.path.dirname(__file__), "static", "gifs")

print(f"Diretório de GIFs esperado: {GIF_FOLDER}")  # Debug

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/luana')
def about():
    return render_template("teste.html")

@app.route("/get_gifs")
def get_gifs():
        # Verifica se a pasta realmente existe antes de tentar listar os arquivos
    if not os.path.exists(GIF_FOLDER):
        print("ERRO: Pasta não encontrada!")
        return jsonify({"error": "Pasta de GIFs não encontrada"}), 500

    print(f"Arquivos encontrados: {os.listdir(GIF_FOLDER)}")  # Debug
    gifs = [f"/static/gifs/{gif}" for gif in os.listdir(GIF_FOLDER) if gif.endswith(".gif")]
    return jsonify(gifs)
