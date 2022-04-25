from users import userInfo
from todos import todos
from posts import posts
from products import items
from comments import comments

userData = userInfo.generateUsers(10)
todoData = todos.generateTodos(10)
postData = posts.generatePosts(10)
productData = items.generateProducts(10)
commentsData = comments.generateComments(10)

fileNames = ["users.json", "todos.json", "posts.json","products.json", "comments.json"]
fileInfo = [userData, todoData, postData, productData, commentsData]

#Generate JSON files for all data
for info in range(len(fileNames)):
    with open("generators/" + fileNames[info], "w") as file:
        file.write(fileInfo[info])
        file.close()
