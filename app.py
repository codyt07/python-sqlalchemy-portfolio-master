from flask import(render_template, redirect,
                url_for, request)
from models import db, Projects, app
from datetime import datetime

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.form:
        pass
    project = Projects.query.all()
    return render_template('index.html', project=project)

@app.route('/project<id>', methods = ['GET', 'POST'])
def project_detail(id):
    detail = Projects.query.get_or_404(id)
    skill = Projects.query.get_or_404(id).skills
    view = skill.split(", ")
    return render_template('detail.html', detail=detail, view=view)


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

def validate_date(capture):
    try:
            product_date_obj = datetime.strptime(capture, '%m-%d-%Y')
            return product_date_obj
    except ValueError:
        print("uh oh")
        
        
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.2")