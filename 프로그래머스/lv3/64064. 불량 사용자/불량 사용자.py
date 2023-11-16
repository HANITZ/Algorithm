from itertools import product

def solution(user_id, banned_id):
    candidates = []
    for banned in banned_id:
        candidate = []
        for user in user_id:
            if len(banned) != len(user):
                continue
            is_matched = True
            for b, u in zip(banned, user):
                if b != '*' and b != u:
                    is_matched = False
                    break
            if is_matched:
                candidate.append(user)
        candidates.append(candidate)
    answers = set()
    for cases in product(*candidates):
        if len(set(cases)) == len(banned_id):
            answers.add(tuple(sorted(cases)))
            
    return len(answers)