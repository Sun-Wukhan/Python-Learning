from flask import Flask, request
from login import do_the_login, show_the_login_form

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST': 
        return do_the_login()
    else: 
        return show_the_login_form()
    
if __name__ == '__main__': 
    app.run(debug=True)