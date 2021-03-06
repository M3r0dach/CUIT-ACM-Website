# -*- coding: utf-8 -*-
from __init__ import *
from util import mdFilter
import datetime
from dao.db import db

# Table of Article
solution_tags = db.Table('solution_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id', ondelete="CASCADE")),
    db.Column('solution_id', db.Integer, db.ForeignKey('solution_article.id', ondelete="CASCADE"))
)

solution_submits = db.Table('solution_submits',
    db.Column('submit_id', db.Integer, db.ForeignKey('submit.id')),
    db.Column('solution_id', db.Integer, db.ForeignKey('solution_article.id'))
)


class SolutionArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    shortcut = db.Column(db.Text)
    content = db.Column(db.Text)
    problem_oj_name = db.Column(db.String(20))
    problem_pid = db.Column(db.String(12))
    last_update_time = db.Column(db.DateTime)
    is_top = db.Column(db.SmallInteger, default=0)
    is_draft = db.Column(db.SmallInteger, default=0)

    # connect to User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="SET NULL"),
                        nullable=True)
    user = db.relationship('User', backref=db.backref('solution', cascade="save-update, merge",
                                                      lazy='dynamic'))

    # connect to Tag
    tags = db.relationship('Tag', secondary=solution_tags,
                           backref=db.backref('solutions', lazy='dynamic'))


    @property
    def md_shortcut(self):
        return mdFilter.markdown(self.shortcut)

    @md_shortcut.setter
    def md_shortcut(self, data):
        self.shortcut = data

    @property
    def md_content(self):
        return mdFilter.markdown(self.shortcut+self.content)

    @md_content.setter
    def md_content(self, data):
        self.content = data

    def __init__(self, title, user):
        self.title = title
        self.user = user
        self.last_update_time = datetime.datetime.now()

    def __repr__(self):
        return '<Article>'


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()