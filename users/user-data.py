import random

from datetime import datetime
import json

firstNames = ["Tracy", "Mclean", "Simon", "Felix", "James", "Princess", "Jane" "Stephan", "Jessica", "Roxanne", "Emma", "Rosemary", "Frank", "Chloe", "Nick", "Portia", "Fanny", "Nicholas", "Bill",
              "Rosa", "Jayden", "Kristein", "Elora", "Christian", "Elena", "John", "Precious", "Emmanuella", "Joella", "Pete", "Bridget", "Kai"]

latitudes = [-43.221, 0.3432, 54.221, 19.002, 18.334, 11.221, -9.3431, 0.331, 5.3314, 0.3385, 9.331, 35.334, 23.23, 33.66,
             12.11, 0.334, 8.92, -3.34001, 3.2241, 0.4522, 0.557, 0.333, 5.34]

longitudes = [3.442, -16.232, 88.223, 13.441, 4.443, 7.659, -2.221, 8.22, 5.42, 5.662, -3.33, 92.34, 0.0012, 7.34,
              8.5564, 14.231, 12.231, 0.0033, 34.334, 21.224, 84.3443, 229.2334]

lastNames = ["Johnson", "Duah", "Sam", "Ofori", "Frick", "Tuchel", "Lampard", "Mount", "Rudiger", "Etornam" "Chilwell", "Kovacic", "Ji", "Jackson", "Parton", "Williams",
             "Debra", "Otoo", "Powell", "Martin", "Frick", "Incoom", "Lukas", 'Havertz', "Clinton", "Smith", "Charlie", "Greatness"]

mailExtension = ["@gmail.com", "@ymail.com", "@xyz.com", "@mailer.com",
                 "@apple.com", "@test.com", "@bby.com", "@somewhere.com"]

occupations = ["Teacher", "Engineer", "Accountant", "Trader", "Businessman", "Programmer", "Beans Seller", "Bedie Wura", "Musician",
               "Technician", "Lawyer", "Politician", "Farmer", "Contractor", "Gob3 Wura", "Comedian", "Waakye Wura", "Footballer", ]

genderGroups = ["Male", "Female", "Trans", "N/A"]

maritalStatuses = ["Single", "Married", "Divorced", "Separated", "Complicated"]

streets = ["Pencil St.", "BX Trio St.", "FishEye St.", "Randomness Lane St.", "Perry Hikes St.",
           "Litos St.", "Fintone St.", "Alfafa St.", "Jane Newman St.", "Michael Jackson St.", "Cryton Avenue"]

photoURLs = ["https://www.nicepng.com/png/detail/741-7413169_placeholder-female.png",
             "https://vitalehealthservices.com/wp-content/uploads/2019/07/male-placeholder-image.jpeg"]

countries = ["USA", "Canada", "Ghana", "Luxembourg", "Algeria", "Nigeria", "Kuwait", "UAE",
             "United Kingdom", "Togo", "China", "Russia", "Ukraine", "Mexico", "Egypt", "Croatia", "Germany", "Poland", "Argentina",
             "France", "Italy", "Spain", "Belgium", "Sweden", "Switzerland", "Finland", "Iceland", "Albania"
             ]

info = []

for d in range(100):
    firstname = random.choice(firstNames)
    lastName = random.choice(lastNames)
    email = firstname.lower() + lastName.lower() + str(random.randint(10, 999)) + \
        random.choice(mailExtension)
    origin = random.choice(countries)
    year = random.randint(1920, 2001)
    dateOfBirth = str(random.randint(0, 29)) + "/" + \
        str(random.randint(1, 12)) + "/" + str(year)
    phoneLine = "(" + str(random.randint(0o1, 276)) + ")" + "-" + \
        str(random.randint(100, 999)) + "-" + str(random.randint(1000, 9999))
    age = datetime.today().year - year
    gender = random.choice(genderGroups)
    photo = photoURLs[0] if gender == "Female" else photoURLs[1]
    job = random.choice(occupations)
    maritalStatus = random.choice(maritalStatuses)

    content = {
        "id": d + 1,
        "name": firstname + " " + lastName,
        "occupation": job,
        "age": age,
        "countryOfOrigin": origin,
        "photoURL": photo,
        "email": email,
        "gender": gender,
        "maritalStatus": maritalStatus,
        "dateOfBirth": dateOfBirth,
        "phoneLine": phoneLine,
        "address": {
            "street": random.choice(streets),
            "cordinates": {
                "latitude": random.choice(latitudes),
                "longitude": random.choice(longitudes)
            }
        }
    }

    info.append(content)


with open("user.json","w") as file:
    file.write(json.dumps({"users": info}))
    file.close()
