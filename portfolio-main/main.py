#Импорт
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
db = SQLAlchemy(app)

@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get("button_html")
    button_db=request.form.get("button_db")

    return render_template('index.html', button_python=button_python , button_discord=button_discord  , button_html=button_html , button_db=button_db )


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(500), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        email = request.form['email']
        text = request.form['text']
        feedback = Feedback(email=email, text=text)
        db.session.add(feedback)
        db.session.commit()
    return render_template('index.html')

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')




    




if __name__ == "__main__":
    app.run(debug=True)




    




