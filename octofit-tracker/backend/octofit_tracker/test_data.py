# This file contains test data for the OctoFit Tracker application.

# Example test data for users, teams, activities, leaderboard, and workouts.

test_users = [
    {"username": "user1", "email": "user1@example.com", "password": "password1"},
    {"username": "user2", "email": "user2@example.com", "password": "password2"},
    {"username": "user3", "email": "user3@example.com", "password": "password3"},
]

test_teams = [
    {"name": "Team Alpha", "members": ["user1", "user2"]},
    {"name": "Team Beta", "members": ["user3"]},
]

test_activities = [
    {"user": "user1", "activity_type": "Running", "duration": "00:30:00"},
    {"user": "user2", "activity_type": "Cycling", "duration": "01:00:00"},
    {"user": "user3", "activity_type": "Swimming", "duration": "00:45:00"},
]

test_leaderboard = [
    {"user": "user1", "score": 100},
    {"user": "user2", "score": 90},
    {"user": "user3", "score": 80},
]

test_workouts = [
    {"name": "Morning Run", "description": "A quick morning run to start the day."},
    {"name": "Evening Cycle", "description": "Cycling session to unwind in the evening."},
    {"name": "Swim Practice", "description": "Swimming practice for endurance."},
]
