import unittest
from RewardApp.utils.db_utils import storeuser, getuserid
from RewardApp.utils.db_utils import storechild, getkidsforuser
from RewardApp.utils.db_utils import storetask, gettasksforuser
from RewardApp.utils.db_utils import storetaskcompl, gettaskscomplforuser
from RewardApp.utils.db_utils import storereward, getrewardsforuser
from RewardApp.utils.db_utils import storerewardcompl, getrewardsredeemedforuser

"""
These test cases rely on the RewardDB_TestData.sql file having been run to insert 
data into the database; as the tests use data from that script 
UserID = 100
ChildID = 101 to 103
TaskID = 120-124
RewardID = 140-143
"""
class Test_db_utils(unittest.TestCase):
#-----------------------
# USER
#-----------------------
# Test adding a user
    def test_store_and_get_user(self):
        store_user = storeuser('Gertrude', 'G7Test@test99.com')
        self.assertIn("User created successfully !", store_user)

        users = getuserid('G7Test@test99.com')
        last_user = users[-1]
        result = last_user[0]
        print(result)
        self.assertIsNotNone(result)

#-----------------------
# CHILD
#-----------------------
#Test adding a new child and then extracting from database
    def test_store_and_get_child(self):
        store_kid = storechild('100', 'Bob')
        self.assertIn("Child created successfully !", store_kid)

        kids = getkidsforuser('100')
        last_kid = kids[-1]  # This will be the last kid added
        expected = 'Bob'
        print(last_kid[0])
        result = last_kid[1]  # The name of last kid added
        self.assertEqual(expected, result)

#-----------------------
# TASK
#-----------------------
# Test adding a new task and then extracting from database
    def test_store_and_get_task(self):
        store_task = storetask('100', 'Write code', '25')
        self.assertIn("Task created successfully !", store_task)

        tasks = gettasksforuser('100')
        last_task = tasks[-1]  # This will be the last task
        expected = 'Write code'
        result = last_task[2]  # The name of last task added
        self.assertEqual(expected, result)

#Test Marking a Task as Complete

    def test_store_and_get_taskcompl(self):

        taskscompl = gettaskscomplforuser('100')
        # we want count for pikachu before test
        for x in taskscompl:
            if x[0] == 'Pikachu':
                count_before = x[2]

        store_taskcompl = storetaskcompl('124', '100', '103')  # Child 103 is Pikachu
        self.assertIn("Task completion created successfully !", store_taskcompl)

        taskscompl2 = gettaskscomplforuser('100')
        # we want count for pikachu after test
        for x in taskscompl2:
            if x[0] == 'Pikachu':
                count_after = x[2]

        self.assertGreater(count_after, count_before)

#-----------------------
# REWARD
#-----------------------
# Test adding a new reward and then extracting from database
    def test_store_and_get_reward(self):
        store_reward = storereward('100', 'Sweet Shop', '10')
        self.assertIn("Reward created successfully !", store_reward)

        rewards = getrewardsforuser('100')
        last_reward = rewards[-1]  # This will be the last reward
        expected = 'Sweet Shop'
        result = last_reward[1]  # The name of last reward added
        self.assertEqual(expected, result)

# Test Redeeming a reward
    def test_store_and_get_rewardcompl(self):

        rewardscompl = getrewardsredeemedforuser('100')
        # reward 143 = Crazy Golf
        # we want count for Crazy Golf before test
        for x in rewardscompl:
            if x[0] == 'Crazy Golf':
                count_before = x[1]

        store_rewardcompl = storerewardcompl('143', '100', '103')  # Child 103 is Pikachu
        self.assertIn("Reward redemption created successfully !", store_rewardcompl)

        rewardscompl = getrewardsredeemedforuser('100')
        # reward 143 = Crazy Golf
        # we want count for Crazy Golf before test
        for x in rewardscompl:
            if x[0] == 'Crazy Golf':
                count_after = x[1]

        self.assertGreater(count_after, count_before)


#-----------------------
# MAIN
#-----------------------
if __name__ == '__main__':
    unittest.main()
