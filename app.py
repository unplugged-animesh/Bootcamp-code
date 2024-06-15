from flask import Flask,render_template,request
from sqlalchemy import or_
from Models.model import *



app=Flask(__name__)

app.config['SECRET_KEY']='East'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///grocery.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_SILENCE_UBER_WARNING']=1

db.init_app(app)


with app.app_context():
    db.create_all()
    
   
    
  
if __name__=="__main__":
    app.run(debug=True)  