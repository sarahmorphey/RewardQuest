create database rewardee;
use rewardee;

CREATE TABLE T_USER (
	user_id BIGINT NOT NULL AUTO_INCREMENT primary key,
	user_name VARCHAR(45) NULL,
	user_username VARCHAR(45) NULL);

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(45),
    IN p_username VARCHAR(45),
    IN p_password VARCHAR(45)
)
BEGIN
    if ( select exists (select 1 from t_user where user_username = p_username) ) THEN

        select 'Username Exists !!';

    ELSE
        insert into t_user
        (
            user_name,
            user_username
        )
        values
        (
            p_name,
            p_username
        );
    END IF;
END$$
DELIMITER ;

CREATE TABLE T_TASK (
	task_id BIGINT NOT NULL AUTO_INCREMENT primary key,
	user_id BIGINT NOT NULL,
	task_desc VARCHAR(50) NOT NULL,
	task_points SMALLINT NOT NULL,
	FOREIGN KEY (user_id) REFERENCES T_USER(user_id));

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createTask`(
    IN p_userid VARCHAR(45),
    IN p_taskdesc VARCHAR(45),
    IN p_taskpoints VARCHAR(45)
)
BEGIN
    if ( select exists (select 1 from t_task where task_desc = p_taskdesc) ) THEN

        select 'Task Exists !!';

    ELSE
        insert into T_TASK
        (
            user_id,
            task_desc,
            task_points
        )
        values
        (
            p_userid,
            p_taskdesc,
            p_taskpoints
        );
    END IF;
END$$
DELIMITER ;

CREATE TABLE T_CHILD (
	child_id BIGINT NOT NULL AUTO_INCREMENT primary key,
	user_id BIGINT NOT NULL ,
	child_name VARCHAR(50) NOT NULL,
	child_points SMALLINT NULL default 0,
	FOREIGN KEY (user_id) REFERENCES T_USER(user_id));


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createChild`(
    IN p_userid VARCHAR(45),
    IN p_childname VARCHAR(50)
)
BEGIN

        insert into t_child
        (
            user_id,
            child_name
        )
        values
        (
            p_userid,
            p_childname
        );

END$$
DELIMITER ;
CREATE TABLE T_TASKCOMPL (
	taskcompl_id BIGINT NOT NULL AUTO_INCREMENT primary key,
	task_id BIGINT NOT NULL,
	user_id BIGINT NOT NULL,
    child_id BIGINT NOT NULL,
	task_date DATE NOT NULL,
	CONSTRAINT T_TASKCOMPL_FK1 FOREIGN KEY (task_id) REFERENCES T_TASK(task_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
	CONSTRAINT T_TASKCOMPL_FK2 FOREIGN KEY (user_id) REFERENCES T_TASK(user_id)
	ON UPDATE CASCADE
    ON DELETE CASCADE,
	CONSTRAINT T_TASKCOMPL_FK3 FOREIGN KEY (child_id) REFERENCES T_CHILD(child_id)
	ON UPDATE CASCADE
    ON DELETE CASCADE);


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createTASKCOMPl`(
    IN p_taskid VARCHAR(45),
    IN p_userid VARCHAR(45),
	IN p_childid VARCHAR(45),
    IN p_taskdate DATE
)
BEGIN

        insert into T_TASKCOMPL
        (
            task_id,
			user_id,
			child_id,
            task_date
        )
        values
        (
            p_taskid,
			p_userid,
			p_childid,
            p_taskdate
        );
/* Hey we need to also read how many points the task is worth and then update child with those points */
	UPDATE T_CHILD
    SET child_points = child_points + (SELECT task_points FROM T_TASK WHERE task_id = p_taskid)
    WHERE child_id = p_childid;
END$$
DELIMITER ;
CREATE TABLE T_REWARD (
	reward_id BIGINT NOT NULL AUTO_INCREMENT primary key,
	user_id BIGINT NOT NULL,
	reward_desc VARCHAR(50) NOT NULL,
	reward_points SMALLINT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES T_USER(user_id));

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createReward`(
    IN p_userid VARCHAR(45),
    IN p_rewarddesc VARCHAR(45),
    IN p_rewardpoints VARCHAR(45)
)
BEGIN
    if ( select exists (select 1 from t_reward where reward_desc = p_rewarddesc) ) THEN

        select 'Reward Exists !!';

    ELSE
        insert into T_REWARD
        (
            user_id,
            reward_desc,
            reward_points
        )
        values
        (
            p_userid,
            p_rewarddesc,
            p_rewardpoints
        );
    END IF;
END$$
DELIMITER ;

CREATE TABLE T_REWARD_REDEEM (
	reward_redeem_id BIGINT NOT NULL AUTO_INCREMENT primary key,
	reward_id BIGINT NOT NULL,
	user_id BIGINT NOT NULL,
    child_id BIGINT NOT NULL,
	reward_date DATE NOT NULL,
	CONSTRAINT T_REWARD_REDEEM_FK1 FOREIGN KEY (reward_id) REFERENCES T_REWARD(reward_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
	CONSTRAINT T_REWARD_REDEEM_FK2 FOREIGN KEY (user_id) REFERENCES T_REWARD(user_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
	CONSTRAINT T_REWARD_REDEEM_FK3 FOREIGN KEY (child_id) REFERENCES T_CHILD(child_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE);


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createREWARD_REDEEM`(
    IN p_rewardid VARCHAR(45),
    IN p_userid VARCHAR(45),
	IN p_childid VARCHAR(45),
    IN p_rewarddate DATE
)
BEGIN

        insert into T_REWARD_REDEEM
        (
            reward_id,
			user_id,
			child_id,
            reward_date
        )
        values
        (
            p_rewardid,
			p_userid,
			p_childid,
            p_rewarddate
        );
/* Hey we need to also read how many points the reward is worth and then update child with those points */
	UPDATE T_CHILD
    SET child_points = child_points - (SELECT reward_points FROM T_REWARD WHERE reward_id = p_rewardid)
    WHERE child_id = p_childid;
END$$
DELIMITER ;

