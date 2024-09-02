from flask import Flask, request, jsonify #type: ignore
app = Flask(__name__)
from Components.registration_function import registration_function
from Components.login_user_function import login_user_function
from Components.account_opening_function import account_opening_function
from Components.loan_opening_function import loan_opening_function
from Components.deposit_opening_function import deposit_opening_function

from ComponentApproval.display_approval_users import display_approval_users
from ComponentApproval.display_single_user import display_single_user
from ComponentApproval.update_approval_user import update_approval_user


@app.route('/', methods=['get'])
def home_function():
    return "The python is up and running"

@app.route('/register_user_route', methods=['POST','OPTIONS'])
def register_user_route():
     return registration_function()

@app.route('/login_user_route', methods=['POST','OPTIONS'])
def login_user_route():
    return login_user_function()

@app.route('/account_open_route', methods=['POST','OPTIONS'])
def account_open_route():
    return account_opening_function()

@app.route('/loan_open_route', methods=['post','OPTIONS'])
def loan_open_route():
    return loan_opening_function()

@app.route('/deposit_open_route', methods=['post','OPTIONS'])
def deposit_open_route():
    return deposit_opening_function()

@app.route('/display_users_for_approval', methods=['GET','OPTIONS'])
def display_users_for_approval():
    return display_approval_users()

@app.route('/display_single_user_route', methods=['GET','OPTIONS'])
def display_single_user_route():
    return display_single_user()

@app.route('/update_approval_user_route', methods=['POST','OPTIONS'])
def update_approval_user_route():
    return update_approval_user()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3011, threaded=False,  use_reloader=False)

