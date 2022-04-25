import json
import random
from .data import comments
import datetime

def generateComments(number):
    commentData = [] 
    for c in range(number):
        comment = random.choice(comments)
        postID = random.randint(1, len(comments))
        userID = random.randint(1, len(comments))
        datePosted = datetime.datetime(random.randint(
            2019, datetime.datetime.now().year), random.randint(1, 12), random.randint(1, 28), random.randint(1, 12), random.randint(1, 59), random.randint(1, 59))
        info = {
            "comment": comment,
            "id": c + 1, 
            "postID": postID, 
            "userID": userID,
            "datePosted": datePosted.ctime()
        }

        commentData.append(info)
    return json.dumps({"comments":commentData})