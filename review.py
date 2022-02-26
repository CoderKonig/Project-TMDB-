from flask import Flask, flash, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import flask
from sqlalchemy import null


@app.route('/reviews', methods=["POST"])
def review():
    return null;