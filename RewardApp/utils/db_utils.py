#===========================================================
# This contains the connection to database and functions
# for inserting / updating / deleting / reading to DB
#===========================================================
import mysql.connector
from RewardApp.utils.config import USER, PASSWORD, HOST #read config file
from flask import json
from  datetime import datetime

DB_NAME = 'rewardee'
class DbConnectionError(Exception):
    pass

def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DB_NAME
    )
    return cnx

# This function takes the extracted data from webform for new user and attempts to insert
# a new user record in the rewardee database after connecting to the database
def storeuser(_name, _email):

    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)

        cur.callproc('sp_createUser', (_name, _email, 'password')) # No password parameter as Auth0 handles it

        result = cur.fetchall()  # this is a list of error messages
        if len(result) is 0:
            db_connection.commit()
            return json.dumps({'message': 'User created successfully !'})
        else:
            print('Error??')
            return json.dumps({'error': str(result[0])})

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# This function takes the extracted data from webform for new task and attempts to insert
# a new task record in the rewardee database after connecting to the database
def storetask(_userid, _desc, _points):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)

        cur.callproc('sp_createTask', (_userid, _desc, _points))

        result = cur.fetchall()  # this is a list of error messages
        if len(result) is 0:
            db_connection.commit()
            return json.dumps({'message': 'Task created successfully !'})
        else:
            return json.dumps({'error': str(result[0])})


        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# This function takes the extracted data from webform for new child and attempts to insert
# a new child record in the rewardee database after connecting to the database
def storechild(_userid, _child):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)

        cur.callproc('sp_createChild', (_userid, _child))

        result = cur.fetchall()  # this is a list of error messages
        if len(result) is 0:
            db_connection.commit()
            return json.dumps({'message': 'Child created successfully !'})
        else:
            return json.dumps({'error': str(result[0])})

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# This function takes the extracted data from webform for a completed task and
# attempts to insert a record in the rewardee database after connecting to the database
def storetaskcompl(_taskid, _userid, _childid):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)

        _date = datetime.today().strftime('%Y-%m-%d')
        cur.callproc('sp_createTaskCompl', (_taskid, _userid, _childid, _date))

        result = cur.fetchall()  # this is a list of error messages
        if len(result) is 0:
            db_connection.commit()
            return json.dumps({'message': 'Task completion created successfully !'})
        else:
            return json.dumps({'error': str(result[0])})

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# This function takes the extracted data from webform for a redeemed reward and
# attempts to insert a record in the rewardee database after connecting to the database
def storerewardcompl(_rewardid, _userid, _childid):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)

        _date = datetime.today().strftime('%Y-%m-%d')
        cur.callproc('sp_createREWARD_REDEEM', (_rewardid, _userid, _childid, _date))

        result = cur.fetchall()  # this is a list of error messages
        if len(result) is 0:
            db_connection.commit()
            return json.dumps({'message': 'Reward redemption created successfully !'})
        else:
            return json.dumps({'error': str(result[0])})

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# This function retrieves a count of completed tasks by child
def gettaskcompl():

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)

        query = """
            SELECT  t2.child_name, count(t1.task_id) 
            FROM t_taskcompl as t1
            join 
            t_child as t2
            ON t1.child_id = t2.child_id
            group by child_name
            """

        cur.execute(query)

        result = cur.fetchall()  # this is a list of error messages
        print(result)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
            return result

# This function retrieves tasks for a user
def gettasksforuser(_userid, html=None):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)

        query = """
            SELECT  user_id, task_id, task_desc, task_points 
            FROM t_task
            where user_id = {};
            """.format(_userid)

        cur.execute(query)

        result = cur.fetchall()
        print(result)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
            if html == 'X':
                task_list = []
                for task in result:
                    r1 = []
                    r1.append(task[1])
                    r1.append(task[2] + ' - ' + str(task[3]) + ' points')
                    task_list.append(r1)
                return task_list
            else:
                return result
# This function takes the extracted data from webform for new reward and attempts to insert
# a new reward record in the rewardee database after connecting to the database
def storereward(_userid, _desc, _points):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)

        cur.callproc('sp_createReward', (_userid, _desc, _points))

        result = cur.fetchall()  # this is a list of error messages
        if len(result) is 0:
            db_connection.commit()
            return json.dumps({'message': 'Reward created successfully !'})
        else:
            return json.dumps({'error': str(result[0])})


        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# This function retrieves a count of completed tasks by child
def gettaskscomplforuser(_userid):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)
        print('GTCFU: ', _userid)
        query = """
            SELECT  t1.child_name, t2.task_desc, count(taskcompl_id) 
            FROM t_taskcompl t3
            join t_task t2 on t3.task_id = t2.task_id
            join t_child t1 on t3.child_id = t1.child_id
            where t3.user_id = {}
            group by t1.child_name, t2.task_desc, t3.child_id;
            """.format(_userid)

        cur.execute(query)

        result = cur.fetchall()
        print(result)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
            return result

# This function retrieves a list of children with completed tasks
def getlistofkidstaskcompl(_userid):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)

        query = """
             SELECT  distinct t2.child_name, t2.child_id
            FROM t_taskcompl t3
            join T_CHILD t2
            on t3.child_id = t2.child_id
            where t3.user_id = {};
            """.format(_userid)

        cur.execute(query)

        result = cur.fetchall()
        print(result)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
            return result

# This function retrieves a list fo task descriptions for completed tasks
def getlistoftasks(_userid):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)

        query = """
            SELECT  distinct t2.task_desc 
            FROM t_taskcompl t3
            join t_task t2 on t3.task_id = t2.task_id
            where t3.user_id = {}
            """.format(_userid)

        cur.execute(query)

        result = cur.fetchall()
        print(result)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
            return result

# This function gets a count of tasks completed by month by child
def getcountoftaskspermonthperchild(_userid):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)

        query = """
            select month(task_date) 'Month', child_id, count(taskcompl_id)
            from t_taskcompl
            where year(task_date) = '2023' and
            user_id = {}
            group by month(task_date), child_id
            order by child_id, 'Month';
            """.format(_userid)

        cur.execute(query)

        result = cur.fetchall()
        print(result)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
            return result

# This function gets the userID by email address
def getuserid(_email):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)
        print("about to query")
        print("email for query is", _email)
        query = """
            SELECT user_id 
            FROM T_USER
            WHERE user_username = '{}' 
            """.format(_email)

        cur.execute(query)

        result = cur.fetchall()
        print(result)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
            return result

# This function gets a list of rewards for a user
def getrewardsforuser(_userid, html=None):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)
        print('I got user', _userid)
        query = """
            SELECT reward_id, reward_desc, reward_points
            FROM T_REWARD
            WHERE user_id = {} 
            """.format(_userid)

        cur.execute(query)

        result = cur.fetchall()
        print(result)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
            if html == 'X':
                reward_list = []
                for reward in result:
                    r1 = []
                    r1.append(reward[0])
                    r1.append(reward[1] + ' - ' + str(reward[2]) + ' points')
                    reward_list.append(r1)
                return reward_list
            else:
                return result

# This function checks if a child has enough points to redeem a reward
def checkkidhasenoughpoints(_rewardid, _childid):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)
        query = """
            SELECT child_points
            FROM T_CHILD
            WHERE child_id = {} 
            """.format(_childid)

        cur.execute(query)

        result = cur.fetchall()
        list = result[0]
        child_points = list[0]
        print('Child ',_childid,  child_points)

        query2 = """
            SELECT reward_points
            FROM T_REWARD
            WHERE reward_id = {} 
            """.format(_rewardid)

        cur.execute(query2)

        result2 = cur.fetchall()
        print('hey did I get more data?', result2)
        list = result2[0]
        reward_points = list[0]
        print('Reward', _rewardid, result2, reward_points)

        if child_points < reward_points:
            cankid = 'N'
        else:
            cankid = 'Y'

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
            return cankid

# This function gets a list of children for a user
def getkidsforuser(_userid, html=None):

    try:

        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DB_NAME)
        print('I got user', _userid)
        query = """
            SELECT child_id, child_name, child_points
            FROM T_CHILD
            WHERE user_id = {} 
            """.format(_userid)

        cur.execute(query)

        result = cur.fetchall()
        print(result)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
            if html == 'X':
                kid_list = []
                for kid in result:
                    r1 = []
                    r1.append(kid[0])
                    r1.append(kid[1] + ' - ' + str(kid[2]) + ' points')
                    kid_list.append(r1)
                return kid_list
            else:
                return result

# This function gets a count of redeemed rewards
def getrewardsredeemedforuser(_userid):

    try:
        db_name = 'rewardee'
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            SELECT reward_desc, COUNT(reward_desc)
            FROM T_REWARD_REDEEM rr
            INNER JOIN T_REWARD r ON r.reward_id = rr.reward_id            
            WHERE rr.user_id = {}
            GROUP BY reward_desc;
            """.format(_userid)

        cur.execute(query)

        result = cur.fetchall()
        print(result)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
            return result

# This function gets the current points for a child
def gettotalpointsavailableforchild(_userid):

    try:
        db_name = 'rewardee'
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            SELECT child_name, child_points
            FROM T_CHILD 
            where user_id = {};
            """.format(_userid)

        cur.execute(query)

        result = cur.fetchall()
        print(result)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
            return result