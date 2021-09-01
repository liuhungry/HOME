from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/first')
def first():
	return render_template('first.html')

@app.route('/second')
def second():
	return render_template('second.html')

@app.route('/third')
def third():
	return render_template('third.html')    

if __name__ == '__main__':
	app.run(host='192.168.10.104',port='5000',debug=True)