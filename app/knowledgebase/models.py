from app import db


class Question(db.Model):
    '''
    Question model - stores a question, the person who wrote it,
    and the channel it belongs to.
    '''

    ''' TABLE NAME '''

    __tablename__ = 'questions'

    ''' ATTRIBUTES '''

    id = db.Column(db.Integer, primary_key=True)

    # Not sure 5000 chars is enough for one question
    text = db.Column(db.String(5000))

    answers = db.relationship('Answer', backref='question', lazy='dynamic')

    comments = db.relationship('Comment', backref='question', lazy='dynamic')

    # integer representing what state the qn is in
    #   - waiting for answers/waiting for votes/rejected/accepted
    state = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))


class Answer(db.Model):
    '''
    Answer model - stores an answer, the votes it has received, the person
    who wrote it, and the question it is responding to.
    '''

    ''' TABLE NAME '''

    __tablename__ = 'answers'

    ''' ATTRIBUTES '''

    id = db.Column(db.Integer, primary_key=True)

    # Not sure 5000 chars is enough for one answer
    text = db.Column(db.String(5000))

    votes = db.relationship('Vote', backref='answer', lazy='dynamic')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))


class Vote(db.Model):
    '''
    Vote model - stores a vote amount, who voted, and either the answer it
    was voting on or the comment is was voting on
    '''

    ''' TABLE NAME '''

    __tablename__ = 'votes'

    ''' ATTRIBUTES '''

    id = db.Column(db.Integer, primary_key=True)

    # Could be negative vote! Take note
    amount = db.Column(db.Integer)

    # who is the voter?
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    answer_id = db.Column(db.Integer, db.ForeignKey('answers.id'))

    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))


class Comment(db.Model):
    '''
    Comment model - stores the id of the user that commented, the question
    it is commenting on, its parent comment, and the cmment itself
    '''

    ''' TABLE NAME '''

    __tablename__ = 'comments'

    ''' ATTRIBUTES '''

    id = db.Column(db.Integer, primary_key=True)

    # enough characters?
    text = db.Column(db.String(5000))

    # who is the commenter?
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    # we need to define a adjacent-list relationship as described
    # in the sqlalchemy docs
    # we have one parent and many children comments
    parent_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    children = db.relationship(
        'Node', backref=db.backref('parent', remote_side=[id]))
