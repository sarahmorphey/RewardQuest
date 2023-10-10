from RewardApp.utils.db_utils import gettaskscomplforuser, getlistofkidstaskcompl,  getlistoftasks


def get_tasks_completed_group_by_child(_userid):
	colours = ['pink', 'yellow', 'blue', 'red', 'green', 'orange', 'purple']
	tasks_compl = gettaskscomplforuser(_userid)
	kids = getlistofkidstaskcompl(_userid)
	tasks = getlistoftasks(_userid)

	names_of_tasks = []
	results = []
	# Create a list of labels of the task descriptions
	for task in tasks:
		names_of_tasks.append(task[0])

# Create a list of dic for each child
	list_kid_datasets = []
	count = 0
	num_tasks = len(names_of_tasks)

	for kid in kids:
		# How many labels
		kid_task_data = [0] * num_tasks

# Create new dict for kid
		new_dict = {
						"label": '',
						"backgroundColor": '',
						"data": []
					}
		new_dict['label'] = kid[0]  # Name of child
		new_dict['backgroundColor'] = colours[count]  # Colour for graph

#       Loop through all records
		for kid_rec in tasks_compl:
			# If current kid then add count data for corresponding task desc
			if kid_rec[0] == kid[0]:
				index = names_of_tasks.index(kid_rec[1])  # This looks for index of task description
				kid_task_data[index] = kid_rec[2]  # This is the count for task
		# After finished with kid - append the dictionary record to a list of the datasets
		new_dict['data'] = kid_task_data
		list_kid_datasets.append(new_dict)
		count += 1

# Add labels as first value in results and then the list of dictionaries
	results.append(names_of_tasks)
	results.append(list_kid_datasets)
	return results
