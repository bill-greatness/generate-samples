import json
import random
import data
import datetime

commentData = [] 
for c in range(80):
    comment = random.choice(data.comments)
    postID = random.randint(1, len(data.comments))
    commentID = random.randint(1, len(data.comments))
    userID = random.randint(1, 20)
    datePosted = datetime.datetime(random.randint(
        2019, datetime.datetime.now().year), random.randint(1, 12), random.randint(1, 28), random.randint(1, 12), random.randint(1, 59), random.randint(1, 59))
    info = {
        "comment": comment,
        "id": commentID, 
        "postID": postID, 
        "userID": userID,
        "datePosted": datePosted.ctime()
    }

    commentData.append(info)
with open("comments.json","w") as file:
    file.write(json.dumps({"comments":commentData}))
    file.close()