#===========================================================
# app.py - This is the main flask app that contains all the
# app routes to control the flow of the web pages.
# It also handles the extraction of data from web forms and
# pass of data when rendering a webpage
#===========================================================
from flask import Flask, json, request, render_template, session, redirect, url_for, jsonify
from dotenv import find_dotenv, load_dotenv
from authlib.integrations.flask_client import OAuth
from authlib.integrations.flask_oauth2 import ResourceProtector
from functools import wraps
from os import environ as env
from urllib.parse import quote_plus, urlencode
from utils.db_utils import storeuser, storetask, storechild, storetaskcompl, gettaskcompl, storereward, gettasksforuser, \
    storerewardcompl, getuserid, getrewardsforuser, getkidsforuser, checkkidhasenoughpoints
from charts.charts import taskscompletedbychild
from charts.charts import taskscompletedbyallchildren
from charts.charts import rewardsredeemedperchild
from charts.charts import taskscompletedovertime
from charts.charts import getpointsavailable

# Setting up ENV file
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# Calling validator to authenticate user
require_auth = ResourceProtector()


# Class for user
class AppUser:
    def __init__(self):
        self.email = None
        self.userid = None

# Instantiate empty User
CurrUser = AppUser()

# Start App
app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")


# Custom decorator to protect endpoints
def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user_info = session.get('user')
        if user_info and 'access_token' in user_info:
            # Access token is present in the session
            return f(*args, **kwargs)
        else:
            # Redirect to login if access token is not in session
            return redirect(url_for("login", next=request.url))
    return decorated

oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

# Entry Point - the first web page served
@app.route('/')
def main():
    user_in_session = "user" in session
    return render_template('index.html', user_in_session=user_in_session)

# Auth0 login
@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token

    # Check if this is valid
    return redirect("/api/signupuser")

# Auth0 logout
@app.route("/logout")
@require_auth
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("main", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )
@app.route("/back_to_login")
def back_to_login():
    return redirect(url_for("login"))

@app.route('/signupCompleted')
def signup_completed():
    return render_template("home.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))

@app.route('/signupcreated')
def signupcreated():
    return render_template('signupcreated.html')

@app.route('/chart')
@require_auth
def chart():
    userobject()
    cdata = gettaskcompl()

    labels = []
    gdata = []
    for item in cdata:
        labels.append(item[0])
        gdata.append(item[1])

    # cvar = createchart(labels, gdata)
    cvar1 = taskscompletedbychild()
    cvar2 = taskscompletedbyallchildren(CurrUser.userid)
    cvar3 = rewardsredeemedperchild(CurrUser.userid)
    cvar4 = taskscompletedovertime(CurrUser.userid)
    cvar5 = getpointsavailable(CurrUser.userid)

    return render_template('chart.html', chart1=cvar1, chart2=cvar2, chart3=cvar3, chart4=cvar4, chart5=cvar5)

@app.route('/homepage')
@require_auth
def homepage():
    return render_template('homepage.html')

@app.route('/tasks')
@require_auth
def tasks():
    return render_template('tasks.html')


@app.route('/taskcreated')
@require_auth
def taskcreated():
    return render_template('taskcreated.html')


@app.route('/displaytasks')
@require_auth
def displaytasks():
    userobject()
    task_list = gettasksforuser(CurrUser.userid, 'X')
    print(task_list)
    return render_template('displaytasks.html', task_list=task_list)

@app.route('/displayrewards')
@require_auth
def displayrewards():
    userobject()
    reward_list = getrewardsforuser(CurrUser.userid, 'X')
    print(reward_list)
    return render_template('displayrewards.html', reward_list=reward_list)
@app.route('/displaychildren')
@require_auth
def displaychildren():
    userobject()
    kid_list = getkidsforuser(CurrUser.userid, 'X')
    print(kid_list)
    return render_template('displaychildren.html', kid_list=kid_list)

@app.route('/taskcompl')
@require_auth
def taskcompl():
    userobject()
    myTasks = gettasksforuser(CurrUser.userid, 'X')
    myKids = getkidsforuser(CurrUser.userid, 'X')
    return render_template('taskcompl.html', myTasks=myTasks, myKids=myKids)

@app.route('/taskcomplcreated')
@require_auth
def taskcomplcreated():
    return render_template('taskcomplcreated.html')


@app.route('/rewards')
@require_auth
def rewards():
    return render_template('rewards.html')

@app.route('/rewardcreated')
@require_auth
def rewardcreated():
    return render_template('rewardcreated.html')


@app.route('/rewardredeemcompl')
@require_auth
def rewardredeemcompl():
    userobject()
    myRewards = getrewardsforuser(CurrUser.userid, 'X')
    myKids = getkidsforuser(CurrUser.userid, 'X')
    return render_template('rewardredeemcompl.html', myRewards=myRewards, myKids=myKids)

@app.route('/rewardredeemcreated')
@require_auth
def rewardredeemcreated():
    return render_template('rewardredeemcreated.html')

@app.route('/rewardredeemerror')
@require_auth
def rewardredeemerror():
    return render_template('rewardredeemerror.html')

@app.route('/child')
@require_auth
def child():
    return render_template('child.html')


@app.route('/childcreated')
@require_auth
def childcreated():
    return render_template('childcreated.html')


# Extract data from webform
@app.route('/api/signupuser', methods=['GET', 'POST'])
def signupuser():  # Capital 'U' in signUp makes this different from web page serving above
    # read the posted values from the UI
    _name = session.get('user', {}).get('userinfo', {}).get('name', '')
    _email = session.get('user', {}).get('userinfo', {}).get('email', '')

    # validate the received values - check all three have a value
    if _name and _email:
        # call db_utils to run the storeuser function
        storeuser(_name, _email)
        # Set email and userid for User object
        CurrUser.email = _email
        user_id =  getuserid(_email)
        user_tup = user_id[0]
        CurrUser.userid =  user_tup[0]
        return redirect(url_for('signupcreated'))
        # return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        print("data issue")
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route('/api/createtask', methods=['GET', 'POST'])
@require_auth
def createtask():
    # read the posted values from the UI
    _desc = request.form['inputDesc']
    _points = request.form['inputPoints']

    # validate the received values - check all have a value
    if _desc and _points:
        # call db_utils to run the storetask function
        userobject()
        storetask(CurrUser.userid, _desc, _points)
        return redirect(url_for('taskcreated'))
        # return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        print("data issue")
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/api/createreward', methods=['GET', 'POST'])
@require_auth
def createreward():
    # read the posted values from the UI
    _desc = request.form['inputDesc']
    _points = request.form['inputPoints']

    # validate the received values - check all have a value
    if _desc and _points:
        # call db_utils to run the storetask function
        userobject()
        storereward(CurrUser.userid, _desc, _points)
        return redirect(url_for('rewardcreated'))
        # return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        print("data issue")
        return json.dumps({'htm'
                           'l': '<span>Enter the required fields</span>'})


@app.route('/api/createchild', methods=['GET', 'POST'])
@require_auth
def createchild():
    # read the posted values from the UI
    _child = request.form['inputChildName']

    # validate the received values - check all have a value
    if _child:
        userobject()
        # call db_utils to run the storechild function
        storechild(CurrUser.userid, _child)
        return redirect(url_for('childcreated', child_name=_child))
        # return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        print("data issue")
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/api/createtaskcompl', methods=['POST'])
@require_auth
def createtaskcompl():
    # read the posted values from the UI
    _taskid = request.form['inputTaskID']
    _childid = request.form['inputChildID']
    # validate the received values exist

    print(_taskid, _childid)


    if _taskid and _childid:
        # call db_utils to run the storetaskcompl function
        userobject()
        storetaskcompl(_taskid, CurrUser.userid, _childid)
        return redirect(url_for('taskcomplcreated'))
        # return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        print("data issue")


@app.route('/api/createrewardredeem', methods=['GET', 'POST'])
@require_auth
def createrewardredeem():
    # read the posted values from the UI
    _rewardid = request.form['inputRewardID']
    _childid = request.form['inputChildID']
    # validate the received values - check all have a value
    if _rewardid  and _childid:
        userobject()
        # call db_utils to run the storerewardcompl function
        canchildredeem = checkkidhasenoughpoints(_rewardid, _childid)
        if canchildredeem == 'Y':
            storerewardcompl(_rewardid, CurrUser.userid, _childid)
            return redirect(url_for('rewardredeemcreated'))
        # return json.dumps({'html':'<span>All fields good !!</span>'})
        else:
            return redirect(url_for('rewardredeemerror'))
    else:
        print("data issue")

def userobject():
    if CurrUser.email == None or CurrUser.userid == None:
        _name = session.get('user', {}).get('userinfo', {}).get('name', '')
        _email = session.get('user', {}).get('userinfo', {}).get('email', '')

        # validate the received values - check all three have a value
        if _name and _email:
            # call db_utils to run the storeuser function
            storeuser(_name, _email)
            # Set email and userid for User object
            CurrUser.email = _email
            user_id =  getuserid(_email)
            user_tup = user_id[0]
            CurrUser.userid =  user_tup[0]

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=env.get("PORT", 3000))
