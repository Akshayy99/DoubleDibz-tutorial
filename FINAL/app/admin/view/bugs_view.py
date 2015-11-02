from flask import flash,redirect,url_for, render_template
from jinja2 import Markup
from wtforms.fields import SelectField, TextAreaField

from flask.ext.admin import BaseView, expose, AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.contrib.sqla.tools import get_query_for_ids
from flask.ext.admin.form import rules
from flask.ext.admin.actions import action
from flask.ext.admin.babel import gettext, lazy_gettext
from flask.ext.admin.contrib.sqla import filters

from flask.ext.login import login_required, login_user, current_user, logout_user
from app.extensions import db, login_manager

from base import SecureModelView

from app.bugposts.models import BugPost

def getAdminBugPostView():
   #auto join user
   BugPost.user = db.relationship("User", uselist=False, lazy='joined')

   return AdminBugPostView(BugPost, db.session)

class AdminBugPostView(SecureModelView):
   page_size = 100
   can_create = False
   can_edit = False
   can_delete = False
   column_list = ('user', 'name', 'description', 'created_at')
   
   def _user(view, context, model, name):
      return model.user.user_name
   
   column_formatters = {
      'user' : _user,
   }