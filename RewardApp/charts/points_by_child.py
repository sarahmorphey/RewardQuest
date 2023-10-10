from RewardApp.utils.db_utils import getkidsforuser


def get_points_by_child(_userid):
	colours = ['pink', 'yellow', 'blue', 'red', 'green', 'orange', 'purple']
	kids = getkidsforuser(_userid)
	kidlabels = []
	kiddata = []
	kidcolours = []
	results = []
	idx = 0

	for kid in kids:
		kidlabels.append(kid[1])
		kiddata.append(kid[2])
		kidcolours.append(colours[idx])
		idx +=1

	results.append(kidlabels)
	results.append(kiddata)
	results.append(kidcolours)
	return results
