from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader #long way to render page, deprecated
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
#from django.utils import simplejson
#from mongoengine import *

from django.contrib.auth import authenticate, login, logout

from django.views.generic import TemplateView

from main.models import People

import urllib
import json

import getpass
import subprocess
#import pexpect
from os.path import expanduser
import os
#import pam
from django.contrib.auth.models import User


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main/index.html'
    def post(self, request, *args, **kwargs):
        render(request, template, {}) 
