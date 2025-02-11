from datetime import datetime

administrator_skills = [
    'Python', 'relational database', 'Software engineering',
    'data science', 'NLP', 'natural language processing', 'Cloud Computing'
]

users = [
    {"id": 1, "username": "petar_mitev", "role": "user", "skills": ["Python", "relational database", "data science"]},
    {"id": 2, "username": "mira_jovanovska", "role": "user", "skills": ["Java", "NLP", "data science"]},
    {"id": 3, "username": "igor_iliev", "role": "user", "skills": ["C++", "data science", "relational database"]},
    {"id": 4, "username": "stole_ristov", "role": "admin", "skills": []}
]

queries = [
    {
        "id": 1,
        "user_id": 1,
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "input_skill_name": "python programming",
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "id": 2,
        "user_id": 2,
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "input_skill_name": "Machine learning",
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
    {
        "id": 3,
        "user_id": 3,
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "input_skill_name": "Cloud Computing",
        "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    },
]

match_results = []
