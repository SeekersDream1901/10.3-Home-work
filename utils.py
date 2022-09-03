import json


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    return load_candidates()


def get_by_pk(pk):
    for candidate in load_candidates():
        if candidate['pk'] == int(pk):
            return candidate
    return 'Not Found'


def get_by_skill(skill_name):
    result = []
    not_found = "Not Found"
    for candidate in load_candidates():
        skills = candidate['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            result.append(candidate)
    return result
