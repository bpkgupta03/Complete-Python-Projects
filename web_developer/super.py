from flask import Flask,render_template,request,redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_file(data):
	with open('database.txt',mode='a') as database:
		email=data['email']
		subject=data['subject']
		msg=data['msg']
		database.write(f'\n {email} {subject} {msg}')

def write_csv(data):
	with open('database.csv',newline='',mode='a') as database2:
		email=data['email']
		subject=data['subject']
		msg=data['msg']
		csv_writer=csv.writer(database2, delimiter=',',quotechar=' ',quoting=csv.QUOTE_MINIMAL)		
		csv_writer.writerow([email,subject,msg])



@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
	if request.method == 'POST':
		data=request.form.to_dict()
		write_csv(data)
		return redirect('/thank_u.html')
	else:
		return 'something went wrong!!!!'
