import os
import json
from flask import Flask, render_template

app = Flask(__name__)

def carregar_casas():
    # Isso garante que o Python encontre o casas.json tanto no seu PC quanto na nuvem da Render
    base_dir = os.path.dirname(os.path.abspath(__file__))
    caminho_json = os.path.join(base_dir, 'casas.json')
    
    try:
        with open(caminho_json, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

@app.route('/')
def home():
    # 1. Lemos a lista com os imóveis e os links das fotos
    dados_casas = carregar_casas()
    # 2. Passamos esses dados para dentro do seu HTML através da variável 'casas'
    return render_template('index.html', casas=dados_casas)

if __name__ == '__main__':
    app.run(debug=True)