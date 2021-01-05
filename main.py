from flask import Flask,redirect,url_for,render_template,request
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("Form.db",check_same_thread=False)
c = conn.cursor()


c.execute('CREATE TABLE IF NOT EXISTS Registration (First_Name TEXT,Last_Name TEXT,Address TEXT,Phone INTEGER)')


@app.route("/",methods=['POST','GET'])
def register():
	print('hi')
	if request.method=='POST':
		FName=request.form["FName"]
		LName=request.form["LName"]
		Address=request.form["Address"]
		phone=request.form["phone"]
		
		print('hi whats up')
		c.execute("INSERT INTO Registration (First_Name,Last_Name,Address,Phone) values (?,?,?,?)",(FName,LName,Address,phone))
		conn.commit()

		return render_template('Show.html')
	else:
		return render_template('Registration.html')




@app.route("/Table")
def table():
		result = c.execute("Select * from Registration")
		result = result.fetchall()
		return render_template('Table.html',result=result)


if __name__ == "__main__":
	app.run()






	