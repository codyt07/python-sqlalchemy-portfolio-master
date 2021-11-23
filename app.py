from flask import(render_template, redirect,
                url_for, request)
from models import db, Projects, app
from datetime import datetime

@app.route('/')
def index():
    project = Projects.query.all()
    return render_template('index.html', project=project)

@app.route('/add_project', methods = ['GET', 'POST'])
def add_project():
    if request.form:
        capture = request.form['date']
        confirmed = validate_date(capture)
        new_project = Projects(title=request.form['title'], date=confirmed,
        description=request.form['desc'], skills = request.form['skills'],               
        url = request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('projectform.html')

@app.route('/proejct/<id>')
def project(id):
    show_projects = Projects.query.get_or_404(id)
    return render_template('index.html', show_projects=show_projects)


def validate_date(capture):
    try:
            product_date_obj = datetime.strptime(capture, '%m-%d-%Y')
            return product_date_obj
    except ValueError:
        print("uh oh")
        
        
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.2")