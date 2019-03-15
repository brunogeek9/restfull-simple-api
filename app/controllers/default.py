import os

from app import app
from app import db
from flask import render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from app.models.tables import Task



