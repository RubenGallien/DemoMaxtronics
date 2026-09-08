from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import json
import os
from mistralai.client import Mistral

print("=== SERVEUR FLASK DEMARRE ===")

app = Flask(__name__)
result = {
	"name": None,
	"jobs": None,
	"children": None,
	"finalPath": None
}


@app.route("/", methods=["GET", "POST"])
def home():
	d = None
	if request.method == "POST":
		path = request.form.get("path")
		fileRec = request.files['file']
		if fileRec and path:
			finalPath = path + '/' + secure_filename(fileRec.filename)
			fileRec.save(finalPath)
			with open(finalPath) as f:
				d = json.load(f)
		if path:
			result["finalPath"] = path + '/patient.json'
		return render_template("form.html", result=d)
	return render_template("index.html")

@app.route("/upload_patient", methods=["POST"])
def upload():
	if request.method == "POST":
		name = request.form.get("name")
		jobs = request.form.get("jobs")
		childrens = request.form.get("childrens")

		jobs_list = jobs.splitlines() if jobs else []
		children_list = childrens.splitlines() if childrens else []

		data = {
			"name": name,
			"jobs": jobs_list,
			"children": children_list
		}

		with open(result["finalPath"], "w", encoding="utf-8") as f:
			json.dump(data, f, ensure_ascii=False, indent=4)

		return "Données enregistrées !"

@app.route("/api_proxy", methods=["POST"])
def mistral():
	if request.method == "POST":
		print("REQUEST:", request.method, request.url)
		print("DATA:", request.data)
		print(os.environ["API_KEY"])
		client = Mistral(api_key=os.environ["API_KEY"])

		response = client.chat.complete(
			model="mistral-small-latest",
			messages=[
				{"role": "user", "content": request.data}
			],
		)

		resp = response.choices[0].message.content
		print(resp)
		return resp
