import random
import datetime
import json
import info


postData = []
for post in range(70):
    title = random.choice(info.titles)
    content = random.choice(info.contents)
    userID = random.randint(1, len(info.contents))
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

with open("post.json", "w") as file:
    file.write(json.dumps({"posts": postData}))
    file.close()
