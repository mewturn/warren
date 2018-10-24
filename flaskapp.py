from flask import Flask, render_template, request, jsonify
import translate
#from flask_sqlalchemy import SQLAlchemy

#mysql = MySQL()

app = Flask(__name__)
#app.config['MYSQL_DATABASE_USER'] = 'milton'
#app.config['MYSQL_DATABASE_PASSWORD'] = ''
#app.config['MYSQL_DATABASE_DB'] = 'myinstance'
#app.config['MYSQL_DATABASE_HOST'] = ''

#mysql.init_app(app)
#conn = mysql.connect()
#cursor = conn.cursor()

@app.route("/", methods=['GET'])
def main():
	return render_template("index.html")

@app.route("/", methods=['POST'])
def process():
	src = request.form['zhsrc']
	model = request.form.get('model')
	src_t = src.replace('"', "'").replace("｠","｠ ").replace("｟"," ｟")
	return render_template("index.html", entgt=translate.translate(src_t, model), zhsrc=src)

@app.route("/translate/<content>", methods=['GET'])
def api_translate(content):
	content_t = content.replace('"', "'").replace("｠","｠ ").replace("｟"," ｟")
	model = "7787"
	return render_template("index.html", entgt=translate.translate(content_t, model), zhsrc=content)
	#return translate._translate(content_t, model="7784")

@app.route("/translate", methods=['GET'])
def _api_translate(model="7787"):
	if not "q" in request.args:
		return "Error."
	content = request.args.get("q").replace('"', "'").replace("｠","｠ ").replace("｟"," ｟")
	if "model" in request.args:
		model = request.args.get("model")
	return translate._translate(content, model)

#@app.route("/feedback", methods=['POST'])
#def feedback():
#	improve = request.form['improve']
#	model = "7785"
#	return render_template("index.html", entgt=translate.translate(improve, model), zhsrc=improve)

# model: which model to translate with, src: source language, tgt: target language, currently all not in use 
#def api_translate(content, model="", src="", tgt=""):
#	if "model" in request.args:
#		model = request.args.get("model")
#	if "src" in request.args:
#		src = request.args.get("src")
#	if "tgt" in request.args:
#		tgt = request.args.get("tgt")
#	# return jsonify(response=translate.translate(content),model=model,source=src,target=tgt)
#	return translate._translate(content)

if __name__ == "__main__":
	app.run()