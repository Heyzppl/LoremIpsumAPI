import lorem
from flask import jsonify, request, render_template



def index():
    return render_template('index.html')

def generate_text():
    size = request.args.get('size', default=1, type=int)
    generated_text = " ".join(lorem.paragraph() for _ in range(size))
    return jsonify({"text": generated_text})

def configure_routes(app):
    app.add_url_rule('/', 'index', index, methods=['GET'])
    app.add_url_rule('/generate-text', 'generate_text', generate_text, methods=['GET'])
