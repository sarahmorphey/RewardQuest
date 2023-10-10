import json
import requests
from RewardApp.charts.tasks_completed_by_child import get_tasks_completed_group_by_child
from RewardApp.charts.pointsavailable import pointsavailable
from RewardApp.charts.rewards_redeemed import rewardsclaimed
from RewardApp.charts.tasks_completed_over_time import get_tasks_completed_group_by_month

def taskscompletedbychild():
        config = {
            "type": "bar",
            "data": {
                "labels": ['Water flowers', 'Dishes', 'Do laundry', 'Iron clothes'],
                "datasets": [{
                    "label": "Tasks Completed by Matilda",
                    "data": [5, 15, 3, 8]
                }]
            },
            "options": {
                "scales": {
                    "xAxes": [{
                        "scaleLabel": {
                            "display": True,
                            "labelString": "Tasks completed"
                        }
                    }],
                    "yAxes": [{
                        "scaleLabel": {
                            "display": True,
                            "labelString": "Number of points"
                        }
                    }]
                }
            }
        }

        postdata = {
            'chart': json.dumps(config),
            'width': 500,
            'height': 300,
            'backgroundColor': 'transparent',
        }

        resp = requests.post('https://quickchart.io/chart/create', json=postdata)
        parsed = json.loads(resp.text)
        print(parsed['url'])
        imglink = ('<img src="' + parsed['url'] + '" alt="A chart showing all tasks completed by a child">')
        return imglink

# to see if the link gets populated
# print(taskscompletedbychild())

def taskscompletedbyallchildren(_userid):
    results = get_tasks_completed_group_by_child(_userid)
#results has labels as first list and then a list of datasets

    config = {
        "type": "bar",
        "data": {
            "labels": results[0],
            "datasets": results[1],
        },
        "options": {
            "scales": {
                "xAxes": [{
                    "stacked": "true",
                    "scaleLabel": {
                        "display": True,
                        "labelString": "Task Description"
                    }
                }],
                "yAxes": [{
                    "stacked": "true",
                    "scaleLabel": {
                        "display": True,
                        "labelString": "Number of Tasks"
                    }
                }]
            }
        }
    }

    postdata = {
        'chart': json.dumps(config),
        'width': 500,
        'height': 300,
        'backgroundColor': 'transparent',
    }

    resp = requests.post('https://quickchart.io/chart/create', json=postdata)
    parsed = json.loads(resp.text)
    print(parsed['url'])
    imglink = ('<img src="' + parsed['url'] + '" alt="A chart showing tasks completed by all children">')
    return imglink


# print(taskscompletedbyallchildren())

def rewardsredeemedperchild(_userid):
    results = rewardsclaimed(_userid)

    config = {
        "type": "pie",
        "data": {
            "labels": results[0],
            "datasets": [{
                "label": "Rewards redeemed all children",
                "data": results[1],
                "backgroundColor": ['pink', 'yellow', 'blue', 'red', 'green', 'orange', 'purple']
            }]
        }
    }

    postdata = {
        'chart': json.dumps(config),
        'width': 500,
        'height': 300,
        'backgroundColor': 'transparent',
    }

    resp = requests.post('https://quickchart.io/chart/create', json=postdata)
    parsed = json.loads(resp.text)
    print(parsed['url'])
    imglink = ('<img src="' + parsed['url'] + '" alt="A chart showing rewards redeemed per child">')
    return imglink

# print(rewardsredeemedperchild())

def taskscompletedovertime(_userid):
    results = get_tasks_completed_group_by_month(_userid)
    config = {
        'type': 'line',
        'data': {
            "labels": results[0],
            "datasets": results[1]
        },
        "options": {
            "scales": {
                "xAxes": [{
                    "scaleLabel": {
                        "display": True,
                        "labelString": "Time period"
                    }
                }],
                "yAxes": [{
                    "ticks": {
                        "beginAtZero": True
                    },
                    "scaleLabel": {
                        "display": True,
                        "labelString": "Number of Tasks completed"
                    }
                }]
            }
        }
    }

    postdata = {
        'chart': json.dumps(config),
        'width': 500,
        'height': 300,
        'backgroundColor': 'transparent',
    }

    resp = requests.post('https://quickchart.io/chart/create', json=postdata)
    parsed = json.loads(resp.text)
    imglink = ('<img src="' + parsed['url'] + '" alt="A chart showing tasks completed over time">')
    return imglink

# print(taskscompletedovertime())

def getpointsavailable(_userid):
    results = pointsavailable(_userid)

    config = {
        "type": "bar",
        "data": {
            "labels": results[0],  # Names of children
            "datasets": [{
                "label": "Points",  # Generic label since we're now comparing children
                "data": results[1],  # Example data: Points completed by each child respectively
                "backgroundColor": ['pink', 'yellow', 'blue', 'red', 'green', 'orange', 'purple'],  # Colors for each child respectively
            }]
        },
        "options": {
            "scales": {
                "xAxes": [{
                    "scaleLabel": {
                        "display": True,
                        "labelString": "Child's Name"
                    }
                }],
                "yAxes": [{
                    "ticks": {
                        "beginAtZero": True
                    },
                    "scaleLabel": {
                        "display": True,
                        "labelString": "Points"
                    }
                }]
            }
        }
    }

    postdata = {
        'chart': json.dumps(config),
        'width': 500,
        'height': 300,
        'backgroundColor': 'transparent',
    }

    resp = requests.post('https://quickchart.io/chart/create', json=postdata)
    parsed = json.loads(resp.text)
    print(parsed['url'])
    imglink = ('<img src="' + parsed['url'] + '" alt="A chart showing points completed by each child">')
    return imglink

# to see if the link gets populated
# print(pointsavailable())