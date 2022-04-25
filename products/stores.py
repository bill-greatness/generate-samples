import random
storeNames = ["Greatness Cooks", "Elora Group", "Alpine Store",
              "Kristein Collections", "Design Theories", "Cookies Cooks", "Lucas Point"]

categories = ["Restaurants", "Pharmacy",
              "Supermarket", "Fashion", "General Goods"]

streets = ["Pencil St.", "BX Trio St.", "FishEye St.", "Randomness Lane St.", "Perry Hikes St.",
           "Litos St.", "Fintone St.", "Alfafa St.", "Jane Newman St.", "Michael Jackson St.", "Cryton Avenue"]

latitudes = [-43.221, 0.3432, 54.221, 19.002,
             18.334, 11.221, -9.3431, 12.11, 0.334, 8.92]

longitudes = [3.442, -16.232, 88.223, 13.441,
              4.443, 7.659, -2.221, 8.5564, 14.231, 12.231]

stores = []
for store in range(5):
    storeID = store + 1
    name = random.choice(storeNames)
    logo = "https://via.placeholder.com/120x120.png"
    category = random.choice(categories)
    numberOfFollowers = random.randint(10, 5000)
    phoneLine = "(" + str(random.randint(0o1, 276)) + ")" + "-" + \
        str(random.randint(100, 999)) + "-" + str(random.randint(1000, 9999))
    openingHours = str(random.randint(1,12)) + ":00 - " + str(random.randint(13,24)) + ":00" 
    address = {
        "street": random.choice(streets),
        "cordinates": {
            "longitude": random.choice(longitudes),
            "lattitude": random.choice(latitudes)
        }
    }

    storeInfo = {
        "name": name,
        "logo": logo,
        "category": category,
        "storeID": storeID,
        "openingHours": openingHours,
        "phoneLine": phoneLine,
        "numberOfFollowers": numberOfFollowers,
        "address": address
    }

    stores.append(storeInfo)

