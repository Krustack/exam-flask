import os
from flask import Flask, render_template, request, redirect
from supabase import create_client, Client

app = Flask(__name__)

def grade_calculation(scores):
    pass

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/add-student', methods=['POST'])
def add_student():
    return redirect('/')

@app.route('/del-student', methods=['POST'])
def del_student():
    return redirect('/')

@app.route('/update-student', methods=['POST'])
def update_student():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)