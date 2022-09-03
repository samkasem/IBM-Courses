from machinetranslation import translator as tr
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    ef=tr.english_to_french(textToTranslate)
    return "Translated text to French is "+ef

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    fe=tr.french_to_english(textToTranslate)
    return "Translated text to English is "+fe

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

