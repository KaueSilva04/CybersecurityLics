from flask import Flask, request, jsonify
from supabase import create_client, Client
from waitress import serve
from flask_cors import CORS

SUPABASE_URL = "https://fzbpunjwrlfzcbkeohkk.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ6YnB1bmp3cmxmemNia2VvaGtrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0MjMyMDkyMywiZXhwIjoyMDU3ODk2OTIzfQ.xnvXQnJ8wvcZdmFaVBmkPCvVT55Q30DA21jKXPJUhII"
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

@app.route('/check-email', methods=['POST'])
def check_email():
    data = request.json
    email =data.get("email")

    if not email:
        return jsonify({"error" : "Campo email vazio"})

    try:
        response = supabase.table("usuario").select("email").eq("email", email).execute()

        if len(response.data) > 0:
            return jsonify({"message": "email ja cadastrado!", "exists": True}), 200
        else:
            return jsonify({"message": "email disponivel", "exists": True}), 200
    
    except Exception as e:
        return jsonify({"error": src(e)}), 500
        





@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email e senha são obrigatórios!"}), 400

    try:
        check_email = supabase.table("usuario").select("email").eq("email", email). execute()

        if len(check_email.data) <= 0:
            # Inserir dados diretamente na tabela do banco de dados
            db_response = supabase.table("usuario").insert({
                "email": email,
                "senha": password  # ATENÇÃO: Nunca armazene senhas em texto plano! Use hashing.
            }).execute()
            # Verificar se há erros na inserção no banco de dados
            if hasattr(db_response, 'error') and db_response.error:
                return jsonify({"error": db_response.error.message}), 400
            # Retornar resposta de sucesso
            return jsonify({
                "message": "Dados registrados com sucesso!",
                "data": {
                    "email": email
                }
            }), 201

        else:
            return jsonify({"mensage": "Esse email ja foi cadastrado"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)