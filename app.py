from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:ENTERPASSWORD@localhost:5432/postgres'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    fname_=db.Column(db.String(120))
    lname_=db.Column(db.String(120))
    ename_=db.Column(db.String(120))
    cname_=db.Column(db.String(120))
    county_=db.Column(db.String(120))
    sleeping_=db.Column(db.String(120))
    depression_=db.Column(db.String(120))
    appetite_=db.Column(db.String(120))
    aches_=db.Column(db.String(120))


    def __init__(self, fname_, lname_, ename_, cname_, county_, sleeping_, depression_, appetite_, aches_):
        self.fname_=fname_
        self.lname_=lname_
        self.ename_=ename_
        self.cname_=cname_
        self.county_=county_
        self.sleeping_=sleeping_
        self.depression_=depression_
        self.appetite_=appetite_
        self.aches_=aches_

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/success/", methods=['POST'])
def success():
    if request.method=='POST':
        fname=request.form["firstname"]
        lname=request.form["lastname"]
        ename=request.form["emailaddress"]
        cname=request.form["mobilenumber"]
        county=request.form["county"]
        sleeping=request.form["group1"]
        depression=request.form["group2"]
        appetite=request.form["group3"]
        aches=request.form["group4"]
        send_email(fname,lname,ename,cname,county,sleeping,depression,appetite,aches)
        print(fname,lname,ename,cname,county,sleeping,depression,appetite,aches)
        if db.session.query(Data).filter(Data.ename_ == ename).count()== 0:
            data=Data(fname,lname,ename,cname,county,sleeping,depression,appetite,aches)
            db.session.add(data)
            db.session.commit()
            return render_template('success.html')
        
    return render_template('index.html', text="Duplicate email address found. Please enter a unique email address.")

if __name__ == "__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=8080)
