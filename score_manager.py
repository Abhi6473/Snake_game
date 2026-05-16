import json
import os
SCORE_FILE = os.path.join(os.path.dirname(__file__), "scores.json")

def load_scores():
    if not os.path.exists(SCORE_FILE):
        return {}
    with open(SCORE_FILE, 'r') as f:
        return json.load(f)

def save_scores(scores):
    with open(SCORE_FILE, 'w') as f:
        json.dump(scores, f, indent=4)

def update_user_score(username, score):
    scores = load_scores()
    if username not in scores or score > scores[username]:
        scores[username] = score
    save_scores(scores)
    return scores[username], max(scores.values())

def get_top_scores(n=5):
    scores = load_scores()
    return sorted(scores.items(), key=lambda x: -x[1])[:n]
