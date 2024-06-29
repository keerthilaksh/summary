from flask import Flask, render_template, request
from text_summary import summarizer 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route( '/', methods=['POST'])
def form():
        rawtext = request.form['rawtext']
        summary,original_length, summary_length= summarizer(rawtext)
        return render_template('index.html' ,summary=summary, original_length=original_length, summary_length=summary_length)
        

if __name__ == "__main__":
    app.run(debug=True)

 