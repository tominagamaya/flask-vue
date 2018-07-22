from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route('/hello/<name>')
def hello_name(name=None):
    return render_template('hello.html', title='flask hello', name=name)


@app.route('/hello', methods=['POST'])
def post():
    if request.method == 'POST':
        name = request.form['post_value']
    else:
        name = "no name."
    return render_template('hello.html', title='flask post', name=name)


@app.route('/get', methods=['GET'])
def get():
    if request.method == 'GET':
        name = request.args.get('name')
    else:
        name = "don't get!"
    return render_template('hello.html', title='flask test', name=name)


@app.route('/')
def hello():
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='XXXXXXXX',
        db='testdb',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )

    cur = db.cursor()
    sql = "select * from members"
    cur.execute(sql)
    members = cur.fetchall()

    cur.close()
    db.close()

    return render_template('hello.html', title='flask test', members=members)


@app.route('/good')
def good():
    name = "Good!!"
    return name


if __name__ == "__main__":
    app.run(debug=True)
