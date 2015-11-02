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
from app.posts.models import BuyRequest

from base import SecureModelView

def getAdminBuyRequestView():
   return AdminBuyRequestView(BuyRequest, db.session)

class AdminBuyRequestView(SecureModelView):
   can_create = False
   can_edit = False
   can_delete = False
   column_searchable_list = ('description', BuyRequest.description)
   column_default_sort = ('created_at' , True)
   column_filters = ('id','description', 'created_at','modified_at')
   
   column_list = ('id', 'name', 'user', 'pictures', 'price', 'description', 'status', 'hashtags')
   
   def _name(view, context, model, name):
      return Markup('<a href="http://www.doubledibz.com/posts/%s" target="_blank">%s</a>' % (model.id, model.name))
   
   def _user(view, context, model, name):
      return Markup('<a href="http://www.doubledibz.com/u/%s" target="_blank">%s</a>' % (model.user.user_name, model.user.user_name))
   
   def _status(view, context, model, name):
      return model.status
      
   def _hashtags(view, context, model, name):
      return [i.name for i in model.hashtags]
   
   column_formatters = {
      'name' : _name,
      'user' : _user,
      'status': _status,
      'hashtags': _hashtags
   }