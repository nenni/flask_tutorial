from app import app, db
from flask import render_template, request, url_for, redirect, g, flash
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, current_user
from .models import User, Role, roles_users, Questions


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/createquestion', methods=['GET', 'POST'])
@login_required
def createquestion():
    if request.method == 'GET':
        return render_template("createquestion.html")

    elif request.method == 'POST':
        try:
            question = str(request.form["question"])
            submitted_answer = str(request.form["submitted_answer"])

            question_answer = Questions(question, submitted_answer)
            db.session.add(question_answer)
            db.session.commit()
            return render_template("questionresponse.html", question=question,
                                   submitted_answer=submitted_answer)
        except Exception as e:
            return render_template(url_for('createquestion'))
    else:
        return redirect(url_for('index'))


@app.route('/answerquestion', methods=['GET', 'POST'])
@app.route('/answerquestion/<int:id>', methods=['GET', 'POST'])
@login_required
def answerquestion(id=None):
    if request.method == 'GET':
        if id:
            question_tbl_entries = Questions.query.filter_by(id=int(id)).first()
            if question_tbl_entries:
                return render_template("answerquestion.html",
                                       question=question_tbl_entries.question,
                                       missing_id=False)
        else:
            return render_template("answerquestion.html", missing_id=True)

    elif request.method == 'POST':

        submitted_id = request.form.get("submitted_id", None)
        # print(submitted_id)

        if submitted_id:
            return redirect(url_for('answerquestion', id=int(submitted_id)))
        else:
            # print(id)
            answer = request.form.get("answer", None)
            # print(answer)
            question_tbl_entries = Questions.query.filter_by(id=int(id)).first()
            # print(question_tbl_entries.answer, answer)
            if question_tbl_entries.answer == answer:
                # print("answers ok")
                return redirect(url_for('index'))
            else:
                # print("answers nok")
                error = 'Invalid answer'
                return render_template('answerquestion.html',
                                       id=id,
                                       question=question_tbl_entries.question,
                                       error=error), 302

    else:
        return redirect(url_for('index'))




