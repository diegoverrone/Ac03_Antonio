
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/exemplo', methods=['POST'])
def exemplo():
    json = request.get_json()
    PrimeiroNome = json['first_name'].upper()
    UltimoNome = json['last_name'].upper()
    time = json['time'].upper()
    papel = json['papel'].upper()
    return jsonify(PrimeiroNome=PrimeiroNome,UltimoNome=UltimoNome,time=time,papel=papel)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port,debug=True)