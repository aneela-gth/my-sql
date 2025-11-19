import json
import os
POST_FILE = "posts.json"
def load_posts():
    if not os.path.exist(POST_FILE):
        return[]
    with open(POST_FILE,"r") as f:
        try:
            return json.load(f)
