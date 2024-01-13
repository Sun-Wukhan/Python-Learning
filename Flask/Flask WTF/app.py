from flask import Flask, render_template, flash, request, redirect, url_for
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6d9056fe62ec54bf2244b5dba59409fe' 


@app.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    if form.validate_on_submit(): 
        
        flash(f'Logged in Successfully as {form.username.data}!', 'SUCCESS')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)
    
@app.route('/')
def home(): 
    return 'Welcome Home!'

if __name__ == '__main__':
    app.run(debug=True)