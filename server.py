from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def eight_by_eight():
    return render_template('index.html', column = 8, row = 8)

@app.route('/<int:num>')
def eight_by_num(num):
    return render_template('index.html', column = num, row = 8)

@app.route('/<int:num1>/<int:num2>')
def num_by_num(num1, num2):
    return render_template('index.html', column = num2, row =num1)

if __name__ == '__main__':
    app.run(debug=True)