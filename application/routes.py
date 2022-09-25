from application import app
from flask import render_template, url_for, redirect,flash, request
from application.form import Expenseform
from application.models import Expense
from application import db
import plotly
import plotly.express as px
import json
import pandas as pd


type = ['Income','Expense']    
category = ['Rent','Salary','Expenditure', 'Others']

@app.route('/')
def index():
    data = db.session.query(Expense).order_by(Expense.date).all()
    return  render_template('report.html', values = data)

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    form = Expenseform()
    if form.validate_on_submit() and request.method == 'POST':
    
        date = str(form.date.data)
        type_form = str(form.type.data)
        cat_form = str(form.category.data)
        amount = str(form.amount.data)
        new_expense = Expense(date = date, type = type_form, category = cat_form, amount = amount)
        db.session.add(new_expense)
        db.session.commit()
        return redirect('/')
    
    else:
        data = Expense.query.all()
        return render_template('submit.html', type = type, cat = category, values =data, form = form)
    
@app.route('/delete/<int:exp_id>', methods = ['GET'])
def delete(exp_id):
    del_id = Expense.query.get_or_404(exp_id)
    db.session.delete(del_id)
    db.session.commit()
    return redirect('/')

@app.route('/dashboard')
def charts():
    income_vs_expense = db.session.query(db.func.sum(Expense.amount), Expense.type).group_by(Expense.type).order_by(Expense.type).all()
    income_vs_cat = db.session.query(db.func.sum(Expense.amount), Expense.category).group_by(Expense.category).order_by(Expense.category).all()
    income_expense = []
    income_cat = []
    
    for total_amount in income_vs_expense:
        income_expense.append(total_amount)
        
    df_1 = pd.DataFrame(income_expense, columns = ['amount', 'type'])  
     
    for total_amount in income_vs_cat:
        income_cat.append(total_amount)
        
    df_2 = pd.DataFrame(income_cat, columns = ['amount', 'category'])
    
    
    #df = pd.read_sql(db.session.query(Expense), db.session.bind)
    fig_1 = px.pie(df_1, values='amount', names='type')
    fig_2 = px.bar(df_2, x='category', y='amount', color = 'category')
    
    
    graph_1 = json.dumps(fig_1, cls=plotly.utils.PlotlyJSONEncoder)
    graph_2 = json.dumps(fig_2, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dash.html', pie_chart = graph_1, bar_graph = graph_2)
    #return '{}'.format(json.dumps(db.session.query(Expense)))