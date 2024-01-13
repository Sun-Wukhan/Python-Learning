from flask import Flask 

app = Flask(__name__)

# Routing to main page
@app.route('/')
def home(): 
    return 'Welcome Flask!'

# Routing to about page
@app.route('/about')
def about(): 
    return "About Page"

# Variable Sections Added to URL 
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

# Logging in route 
@app.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        return do_the_login()
    else: 
        return show_the_login_form()

if __name__ == '__main__': 
    app.run(debug=True)
    
