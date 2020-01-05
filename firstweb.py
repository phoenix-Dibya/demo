from flask import Flask ,render_template

app = Flask(__name__) #

@app.route('/') #redirect the webpage to specific url

def home():
	return render_template('home.html')  #render_template redirects to a html page you have created like here home.html


@app.route('/about/') #redirect the webpage to specific url

def about():
	return render_template('about.html')

if __name__ == '__main__':  #case 1 when a script is executed
									#__name__ == "__main__"
	app.run(debug=True)     #case 2 when a script is imported
									#__name__ =="firstweb"



