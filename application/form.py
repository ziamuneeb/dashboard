from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, Optional, ValidationError

class Expenseform(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                                choices=[('income', 'income'),
                                        ('expense', 'expense')])
    category = SelectField("Category", validators=[DataRequired()],
                                            choices =[('rent', 'rent'),
                                            ('salary', 'salary'),
                                            ('investment', 'investment'),
                                            ('side_hustle', 'side_hustle')
                                            ]
                            )
    amount = IntegerField('Amount', validators = [DataRequired()])    
    date = DateField('Date', format = '%Y-%m-%d', validators=[DataRequired()])                               
    submit = SubmitField('Generate Report')   



'''class Expenseform(FlaskForm):
    amount = StringField(validators=[DataRequired(), Length(min = 4, max = 20)], render_kw={'placeholder': 'Amount'})
    type = StringField(validators=[DataRequired(), Length(min = 4, max = 20)], render_kw={'placeholder': 'Type'})
    category = StringField(validators=[DataRequired(), Length(min = 4, max = 20)], render_kw={'placeholder': 'Category'})
    submit = SubmitField('Submit')  '''                        