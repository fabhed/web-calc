from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operator = request.form.get('operator')

        calculator = Calculator()
        result = calculator.calculate(num1, num2, operator)

        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
