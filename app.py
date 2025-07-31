from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    src_lang = data['source']
    tgt_lang = data['target']
    text = data['text']

    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{src_lang}|{tgt_lang}"
    }

    try:
        response = requests.get(url, params=params)
        response_data = response.json()

        translated_text = response_data['responseData']['translatedText']
        return jsonify({'translated_text': translated_text})
    
    except Exception as e:
        print("Translation error:", e)
        return jsonify({'translated_text': "Translation failed. Try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)
