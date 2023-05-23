from flask import Flask, render_template
#initiate app flask incident
app = Flask(__name__)

jobs = [{
  'id':1,
  'title':'Data Analyst',
  'location':'Mbabane',
  'salary': 'E600,000'
},{
      'id':2,
      'title':'Data Scientist',
      'location':'Mbabane',
      'salary': 'E800,000'},
       {
           'id':3,
  'title':'Credit Analyst',
  'location':'Ezulwini',
  'salary': 'E400,000'
       }]
#provide route
@app.route('/')
#define a function
def home():
  return render_template('home.html', jobs=jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=8080)