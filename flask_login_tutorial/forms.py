"""Sign-up & log-in forms."""
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
import re
def format(form, field):
     # Check for at least 1 uppercase letter
    if not re.search(r'[A-Z]', field.data):
        flash("Password must contain at least 1 uppercase letter.", 'error')
        
    
    # Check for at least 1 lowercase letter
    if not re.search(r'[a-z]', field.data):
        flash("Password must contain at least 1 lowercase letter.", 'error')
        
    
    # Check for at least 1 number
    if not re.search(r'\d', field.data):
        flash("Password must contain at least 1 number.", 'error')
        
    
    # Check for at least 1 special character
    if re.search(r'[^A-Za-z0-9]', field.data):
        flash("Password must contain at least 1 special character.", 'error')
        
    # Password meets all criteria
        return True

class SignupForm(FlaskForm):
    """User Sign-up Form."""

    name = StringField("Name", validators=[DataRequired()])
    email = StringField(
        "Email",
        validators=[
            Length(min=6),
            Email(message="Enter a valid email."),
            DataRequired(),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, message="Select a stronger password."),
            format,
        ],
    )
    confirm = PasswordField(
        "Confirm Your Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )
    website = StringField("Website", validators=[Optional()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    """User Log-in Form."""

    email = StringField("Email", validators=[DataRequired(), Email(message="Enter a valid email.")])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")
