import unittest
import requests_mock
from charts import taskscompletedbychild
from charts import taskscompletedbyallchildren
from charts import rewardsredeemedperchild
from charts import taskscompletedovertime
from charts import getpointsavailable

class TestCharts(unittest.TestCase):
    @requests_mock.Mocker()
    def test_taskscompletedbychild(self, m):
        # Mocking the post request response
        mock_response = {
            "url": "https://mocked_url.com"
        }
        m.post('https://quickchart.io/chart/create', json=mock_response)

        # Calling the function
        result = taskscompletedbychild()

        expected_img_link = '<img src="https://mocked_url.com" alt="A chart showing all tasks completed by a child">'
        self.assertEqual(result, expected_img_link)

    # Added print statement for my own benefit
    # print(test_taskscompletedbychild)


    @requests_mock.Mocker()
    def test_taskscompletedbyallchildren(self, m):
        mock_response = {
            "url": "https://mocked_url.com"
        }
        m.post('https://quickchart.io/chart/create', json=mock_response)

        result = taskscompletedbyallchildren('100')

        expected_img_link = '<img src="https://mocked_url.com" alt="A chart showing tasks completed by all children">'
        self.assertEqual(result, expected_img_link)
    # print(test_taskscompletedbyallchildren)
    @requests_mock.Mocker()
    def test_rewardsredeemedperchild(self, m):
        mock_response = {
            "url": "https://mocked_url.com"
        }
        m.post('https://quickchart.io/chart/create', json=mock_response)

        result = rewardsredeemedperchild('100')

        expected_img_link = '<img src="https://mocked_url.com" alt="A chart showing rewards redeemed per child">'
        self.assertEqual(result, expected_img_link)

    # print(test_rewardsredeemedperchild)

    @requests_mock.Mocker()
    def test_taskscompletedovertime(self, m):
        mock_response = {
            "url": "https://mocked_url.com"
        }
        m.post('https://quickchart.io/chart/create', json=mock_response)

        result = taskscompletedovertime('100')

        expected_img_link = '<img src="https://mocked_url.com" alt="A chart showing tasks completed over time">'
        self.assertEqual(result, expected_img_link)

    # print(test_taskscompletedovertime)
    @requests_mock.Mocker()
    def test_getpointsavailable(self, m):
        # Mocking the post request response
        mock_response = {
            "url": "https://mocked_url.com"
        }
        m.post('https://quickchart.io/chart/create', json=mock_response)

        result = getpointsavailable('100')

        expected_img_link = '<img src="https://mocked_url.com" alt="A chart showing points completed by each child">'
        self.assertEqual(result, expected_img_link)
    # print(test_pointsavailable)

if __name__ == '__main__':
    unittest.main()