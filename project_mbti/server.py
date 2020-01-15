from flask import Flask, request, render_template, url_for
from function import final_output,twitter_setup,get_posts
import os

PEOPLE_FOLDER = os.path.join('static', 'image')

app = Flask(__name__)
app.config["UPLOAD_FOLDER"]=PEOPLE_FOLDER
@app.route("/main")
def home():
    
    return render_template("index.html")

@app.route("/result",methods=["POST"])
def output():
	form_data = request.form
	if form_data == '':
		return render_template("index.html",str_="Input Needed!!!!")
	else:
		posts=""
		name = form_data["text"] 
		number=50
		posts=get_posts(name,number)
		if len(posts)==0:
			return render_template("index.html",str_="Enter correct user name")
		status = final_output(posts)
		return render_template("index.html",str_=status)

if __name__ == "__main__":
    app.run(debug=True)
