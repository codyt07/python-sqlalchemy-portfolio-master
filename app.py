from flask import(render_template, redirect,
                url_for, request)
from models import db, Projects, app
from datetime import datetime

@app.route('/')
def index():
    project = Projects.query.all()
    return render_template('index.html', project=project)

@app.route('/project/<id>', methods = ['GET', 'POST'])
def project_detail(id):
    detail = Projects.query.get_or_404(id)
    skill = Projects.query.get_or_404(id).skills
    view = skill.split(", ")
    return render_template('detail.html', detail=detail, view=view)


@app.route('/project/new', methods = ['GET', 'POST'])
def new():
    if request.form:
        capture = request.form['date']
        sql_happy = datetime.strptime(capture, '%Y-%m')
        new_project = Projects(title=request.form['title'], date=sql_happy,
            description=request.form['desc'], skills = request.form['skills'],               
            url = request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('projectform.html')

@app.route('/project/<id>/edit', methods = ['GET', 'POST'])
def edit(id):
    edit = Projects.query.get_or_404(id)
    return render_template('edit.html', edit=edit)

@app.route('/project/<id>/delete', methods=['GET', 'POST'])
def delete(id):
    delete = Projects.query.get_or_404(id)
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.2")