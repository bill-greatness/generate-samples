import random
import datetime
from .info import contents, titles
import json

def generatePosts(number):
    postData = []
    for post in range(number):
        title = random.choice(titles)
        content = random.choice(contents)
        userID = random.randint(1, len(contents))
        postID = post + 1
        datePosted = datetime.datetime(random.randint(
            2019, datetime.datetime.now().year), random.randint(1, 12), random.randint(1, 28), random.randint(1, 12), random.randint(1, 59), random.randint(1, 59))
        photoURL = "https://via.placeholder.com/" + \
            str(random.randint(500, 800)) + "x" + \
            str(random.randint(120, 300)) + ".png"
        data = {
            "title": title.title(),
            "content": content,
            "userID": userID,
            "photoURL": photoURL,
            "postID": postID,
            "datePosted": datePosted.isoformat()
        }
        postData.append(data)
    return json.dumps({"posts":postData})
