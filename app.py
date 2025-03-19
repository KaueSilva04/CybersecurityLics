from flask import Flask, request, jsonify, render_template
from waitress import serve  # Importe o Waitress
from supabase import create_client, Client
import os
from flask_cors import CORS

SUPABASE_URL = "https://fzbpunjwrlfzcbkeohkk.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ6YnB1bmp3cmxmemNia2VvaGtrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDIzMjA5MjMsImV4cCI6MjA1Nzg5NjkyM30.O0O-ypXn7EvnQnGE0cq6dDcEnQuJ-oFVk4m902QQKqI"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)
CORS(app)
# Testar conexão listando tabelas do banco
try:
    response = supabase.table("usuario").select("*").limit(1).execute()
    print("Conexão bem-sucedida! 🎉")
    print(response.data)
except Exception as e:
    print("Erro na conexão:", e)


@app.route('/')
def home():
    return "Servidor Flask no Render está rodando!"


# Rota de registro
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email e senha são obrigatórios!"}), 400

    try:
        # Criar usuário no Supabase Auth
        response = supabase.auth.sign_up({"email": email, "password": password})

        if "error" in response:
            return jsonify({"error": response["error"]["message"]}), 400

        return jsonify({"message": "Usuário registrado com sucesso!", "user": response["user"]}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Rodando a aplicação com o Waitress, não com o Flask
    serve(app, host='0.0.0.0', port=5000)
