from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db. Column('Created', db.DateTime, default = datetime.datetime.now)
    title = db.Column('Title', db.String())
    date = db.Column('Date', db.Date())
    skills= db.Column('Skills', db.String())
    description = db.Column('Description', db.Text())
    url = db.Column('URL', db.Text())                    
    
    def __repr__(self):
        return f''' <Projects(Title: {self.title}
            Date: {self.date}
            Skills: {self.skills}
            Description: {self.description}
            '''
    