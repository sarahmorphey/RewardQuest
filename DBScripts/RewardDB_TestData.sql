 use rewardee;
 /* Insert entries into T_USER */
         insert into t_user
        (
            user_id,
            user_name,
            user_username
        )
        values
        (
            '100', 'Tester', 'G7tester@test.com'
        );
/* Insert entries into T_CHILD */
       insert into t_child
        (
            child_id,
            user_id,
            child_name,
            child_points
        )
        values
        ('101', '100', 'Alexandra', '150'),
        ('102', '100', 'Ash', '120'),
        ('103', '100', 'Pikachu', '750');

/* Insert entries into T_TASK */
insert into t_task
        (
			task_id,
            user_id,
            task_desc,
            task_points
        )
        values
        ('120', '100', 'Water flowers','5'),
        ('121', '100', 'Wash Dishes','5'),
        ('122', '100', 'Clean Bedroom','5 '),
        ('123', '100', 'Wash Car','10'),
        ('124', '100', 'Vacuum Stairs','10')
        ;
/* Insert entries into T_TASKCOMPL */
insert into t_taskcompl
        (
            task_id,
			user_id,
			child_id,
            task_date
        )
        values
        ('120', '100', '101','2023-01-06'),
		('120', '100', '101','2023-01-17'),
        ('120', '100', '101','2023-02-06'),
		('120', '100', '101','2023-02-14'),
		('120', '100', '101','2023-03-14'),
		('121', '100', '102','2023-04-16'),
		('121', '100', '102','2023-05-11'),
        ('123', '100', '102','2023-02-09'),
		('123', '100', '102','2023-03-15'),
        ('123', '100', '102','2023-04-19'),
		('123', '100', '102','2023-05-26'),
		('122', '100', '102','2023-02-10'),
        ('122', '100', '102','2023-03-19'),
		('122', '100', '102','2023-04-06'),
        ('122', '100', '102','2023-07-29'),
		('122', '100', '102','2023-05-20'),
		('122', '100', '102','2023-05-12'),
		('122', '100', '102','2023-05-29'),
        ('121', '100', '102','2023-04-17'),
		('123', '100', '102','2023-07-28'),
        ('123', '100', '102','2023-03-30'),
		('120', '100', '102','2023-05-10'),
		('120', '100', '102','2023-03-10'),
		('120', '100', '102','2023-02-26'),
        ('120', '100', '103','2023-01-06'),
		('120', '100', '103','2023-06-17'),
        ('120', '100', '103','2023-02-06'),
		('120', '100', '103','2023-02-14'),
		('120', '100', '103','2023-03-14'),
		('120', '100', '103','2023-04-06'),
		('120', '100', '103','2023-05-06'),
		('120', '100', '103','2023-08-10'),
		('120', '100', '103','2023-08-26');

/* Insert entries into T_REWARD */
insert into t_reward
        (
			reward_id,
            user_id,
            reward_desc,
            reward_points
        )
        values
        ('140', '100', 'Disneyland Paris','600'),
        ('141', '100', 'Waterpark','120'),
        ('142', '100', 'Icecream at the beach','5'),
        ('143', '100', 'Crazy Golf','10')
        ;

/* Insert entries into T_REWARD_REDEEM */
insert into t_reward_redeem
        (
            reward_redeem_id,
            reward_id,
			user_id,
			child_id,
            reward_date
        )
        values
        ('130', '142', '100', '101','2023-01-06'),
		('131', '143', '100', '101', '2023-01-17'),
        ('132', '142', '100', '101', '2023-02-06'),
		('133', '141', '100', '103','2023-02-14'),
		('134', '142', '100', '103','2023-03-14'),
		('135', '143', '100', '101','2023-04-06'),
        ('136', '141', '100', '102','2023-01-13'),
        ('137', '141', '100', '101','2023-08-25'),
        ('138', '141', '100', '102','2023-08-25'),
        ('139', '141', '100', '103','2023-08-25');