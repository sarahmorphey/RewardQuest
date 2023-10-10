# Group-7-Reward-Project

## Description

### Welcome to RewardQuest!
RewardQuest is an interactive web application designed to empower parents and caregivers in nurturing their children's growth through positive reinforcement and achievement tracking. Our platform transforms everyday tasks and responsibilities into exciting opportunities for personal development and celebration.

### Features

- **Child Profiles:** Create personalised profiles for each child, tailoring tasks and rewards to their unique interests and needs.

- **Task Management:** Easily set up tasks that align with your child's routines and responsibilities. Assign points to tasks to encourage completion.

- **Reward System:** Foster a sense of achievement and responsibility by allowing children to choose rewards based on the points they earn from completed tasks.

- **Visual Progress Tracking:** Interactive charts provide a visual snapshot of your child's accomplishments and milestones, fostering a sense of accomplishment for both parents and children.

- **User-Friendly Interface:** Our intuitive interface makes it simple for parents and children to manage tasks, rewards, and track progress.

## Installation

1. Open the project in PyCharm
2. Run all the DB scripts in MySQL - RewardDB_Create and RewardDB_TestData
3. In Pycharm, Install all packages that are required
4. Enter your MySQL password in config.py
5. Run App.py
6. Click on the first link in the run panel (http://127.0.0.1:3000)
7. You will be redirected to the home-page website in your browser
8. To use all functionality of the app, please sign up and log in using the Sign Up/Log In button

## To log in:
- You can create your own account by signing up, which will then give you access to all functionality including adding children, adding tasks and adding rewards
- To show all functionality of the app, we have created a test case user that already has children attached to it, who have been set tasks, completed tasks and had rewards added. You will be able to view charts showing all data connected to this account in the charts tab.
- To log on as our test user please use the following details:
> Email address: G7tester@test.com
>
> Password: G7testing

## Testing
 - a user is created in the DB Test Data: G7tester@test.com G7testing
 - there are chart test cases in Charts folder
 - there are DB Utils test cases in Utils folder

_Please note:_ The .env file typically shouldn't be on GitHub as it contains confidential information. However, as this
is a private repo and for the ease of running this project, the .env file has been added.

## Project log
https://docs.google.com/spreadsheets/d/1fSs_QQJwQGcOsF2paid3kiy0SseL8D7CyYl8-XySLOM/edit#gid=0