from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Laden der Vokabelliste aus einer CSV-Datei
vokabeln = [
    {"deutsch": "Haus", "fremdsprache": "House"},
    {"deutsch": "Auto", "fremdsprache": "Car"},
    # Hier Vokabeln hinzufügen oder aus einer CSV-Datei laden
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_random_vokabel', methods=['GET'])
def get_random_vokabel():
    random_vokabel = random.choice(vokabeln)
    return jsonify(random_vokabel)

@app.route('/check_antwort', methods=['POST'])
def check_antwort():
    data = request.get_json()
    vokabel_deutsch = data['deutsch']
    antwort = data['antwort']
    for vokabel in vokabeln:
        if vokabel['deutsch'] == vokabel_deutsch:
            if vokabel['fremdsprache'].lower() == antwort.lower():
                return jsonify({"correct": True})
            else:
                return jsonify({"correct": False})
    return jsonify({"correct": False})

if __name__ == '__main__':
    app.run(debug=True)