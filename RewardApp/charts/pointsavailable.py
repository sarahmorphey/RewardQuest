from RewardApp.utils.db_utils import gettotalpointsavailableforchild

def pointsavailable(_userid):
    results = gettotalpointsavailableforchild(_userid)

    chartlabel = []
    chartvalues = []
    returnvalue = []

    for result in results:
        chartlabel.append(result[0])
        chartvalues.append(result[1])

    returnvalue.append(chartlabel)
    returnvalue.append(chartvalues)

    return returnvalue