from flask import Flask, render_template, request, redirect
from dbManager import DBManager

app = Flask(__name__)

db = DBManager(
    dbname="kodland",
    user="zeynep2332",
    password="ikibin25",
    host="zeynep2332.mysql.pythonanywhere-services.com",
    port=3306
)


db.cr_table()

@app.route('/', methods=['GET', 'POST'])
def quiz_template():
    if request.method == 'POST':
        try:
            username = request.form['username']
            color = request.form['question1']
            animal = request.form['question2']
            hobbies = request.form['question3']

            db.insert(username, color, animal, hobbies)

            return redirect('/submitted')
        except Exception as e:
            return f"ERROR: {e}"

    return render_template('quiz_template.html')

if __name__ == '__main__':
    app.run(debug=True)

