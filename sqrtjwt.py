from flask import Flask, request, jsonify
import math
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'uptc2025'  
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    print("Prueba")
    username = request.json.get('username')
    password = request.json.get('password')
    
    if username == 'jorge' and password == '12345':  
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    
    return jsonify({'error': 'Credenciales inválidas'}), 401

@app.route('/sqrt', methods=['GET'])
@jwt_required()
def calcular_raiz():
    print("Verificando cambios en git")
    try:
        numero = float(request.args.get('numero'))
        if numero < 0:
            return jsonify({'error': 'No se puede calcular la raíz cuadrada de un número negativo'}), 400
        resultado = math.sqrt(numero)
        return jsonify({'numero': numero, 'raiz_cuadrada': resultado})
    except (TypeError, ValueError):
        return jsonify({'error': 'Parámetro inválido, se requiere un número'}), 400

if __name__ == '__main__':
    app.run(debug=True)
