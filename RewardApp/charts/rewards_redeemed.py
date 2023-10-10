from RewardApp.utils.db_utils import getrewardsredeemedforuser

def rewardsclaimed(_userid):
    results = getrewardsredeemedforuser(_userid)

    chartlabel = []
    chartvalues = []
    returnvalue = []

    for result in results:
        chartlabel.append(result[0])
        chartvalues.append(result[1])

    returnvalue.append(chartlabel)
    returnvalue.append(chartvalues)

    return returnvalue