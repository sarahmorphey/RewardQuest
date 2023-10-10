from RewardApp.utils.db_utils import gettaskscomplforuser, getlistofkidstaskcompl,  getlistoftasks, getcountoftaskspermonthperchild


def get_tasks_completed_group_by_month(_userid):
	colours = ['pink', 'yellow', 'blue', 'red', 'green', 'orange', 'purple']
	tasks_count = getcountoftaskspermonthperchild(_userid)
	kids = getlistofkidstaskcompl(_userid)

	names_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	results = []

# Create a list of dic for each child
	list_kid_datasets = []
	count = 0
	for kid in kids:
		#print('Creating dict for: ', kid[0])
# Create new dict for kid
		new_dict = {
						"label": '',
						"borderColor": '',
						"backgroundColor": '',
						"fill": 'false',
						"data": []
					}
		new_dict['label'] = 'Cumulative Tasks Completed by ' + kid[0]  # Name of child
		new_dict['borderColor'] = colours[count]  # Colour for graph
		new_dict['backgroundColor'] = colours[count]  # Colour for graph
#       Loop through all records
		kid_task_count = [0] * 12  # 12 entries for month
		for cnt in tasks_count:
			if cnt[1] == kid[1]:
				#print('cnt: ', cnt[0])
				#print('kid: ', kid[0])
				kid_task_count[cnt[0]-1] = cnt[2]  # Count into month_index
		# No change count to be added up
		#print(kid_task_count)
		for idx in range(12):
			kid_task_count[idx] = kid_task_count[idx] + kid_task_count[idx - 1]

		#print(kid_task_count)

		new_dict['data'] = kid_task_count  # Colour for graph
		list_kid_datasets.append(new_dict)
		count +=1

# Add labels as first value in results and then the list of dictionaries
	results.append(names_of_months)
	results.append(list_kid_datasets)
	return results
