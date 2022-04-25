from datetime import datetime
import random
import json

todos = [
    "Buy Biscuits for Kids",
    "Debug Python Script", 
    "Do Nothing",
    "Write Code in Notepad",
    "Brush my Teeth",
    "Visit my grandparents",
    "Look for a girlfriend",
    "Design UI of Application","Do the Dishes",
    "Read more about Jordan Peterson",
    "Watch The Blacklist",
    "Turn of light",
    "Prepare pencil Takes",
    "Talk to Bjarne about pointers",
    "Turn Computer Off",
    "Find My Watch",
    "Talk to Kids about Programming",
    "Convince James about learning C++", 
    "Relax",
    "Learn to Play Piano", 
    "Wear My Spectacles",
    "Wander Around",
    "Get Tired",
    "Spend time with Family",
    "Learn about physics",
    "buy cookies at restaurant", 
    "pay dues to the boss",
    "Do some refactoring",
    "make some hot tea",
    "walk 20 meters to the coast"
]

statuses = ["Completed", "New", "Staled", "Cancelled"]


def generateTodos(number):
    info = []
    for x in range(number):
        genDate = datetime(datetime.now().year, datetime.now().month, random.randint(
            1, 20), random.randint(1, 12), random.randint(10, 59), random.randint(3, 59))
        todo = random.choice(todos)
        status = random.choice(statuses)
        time = genDate.ctime()
        userID = random.randint(1, len(todos))

        content = {
            "id": x + 1,
            "activity": todo.title(),
            "status": status,
            "time": time,
            "userID":userID
        }

        info.append(content)
    return json.dumps({"todos":info})
