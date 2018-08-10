from flask import Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app =Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://saharsh:saharsh@localhost/saharsh'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://ealjwezyboygbs:33a86d136be843dd9b44f3bab835ee293fe1cc570b4fdf1a8b4c5919d899160d@ec2-54-225-76-201.compute-1.amazonaws.com:5432/d6lq10srd6ftef?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email_=db.Column(db.String(120),unique=True)
    height_=db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email_=email_
        self.height_=height_

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form['email_name']
        height=request.form['height_name']
        print(email,height)

        if db.session.query(Data).filter(Data.email_==email).count()==0:

            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height,1)
            count=db.session.query(Data.height_).count()
            send_email(email,height,average_height,count)
            return render_template('success.html')
    return render_template('index.html',
    text="Seems like you already submitted.?")

if __name__=='__main__':
    app.debug=True
    app.run()
