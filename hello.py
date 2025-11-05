
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["alpemones"]
players = db["players"] #collection of players

battles = db["battles"] #collection of battles

def get_alpemons_by_type(username: str, type_name: str):
    """
    Return list of alpemons of `type_name` for user `username` using aggregation ($filter).
    """
    pipeline = [
        {"$match": {"name": username}},
        {"$project": {
            "_id": 0,
            "alpemons": {
                "$filter": {
                    "input": "$alpemons",
                    "as": "a",
                    "cond": {"$eq": ["$$a.type", type_name]}
                }
            }
        }}
    ]
    docs = players.aggregate(pipeline)
    return docs


try:
    database = client.list_database_names()
    
    # players.insert_one(
    #     {
    #         "name": "Player1",
    #         # outfit and physical attributes as an avatar object
    #         "outfit": {
    #             "hat": "hat1.jpg",
    #             "shirt" : "shirt1.jpg",
    #             "pants": "pants1.jpg",
    #             "accessory": "glasses1.jpg",
    #             "shoes": "shoes1.jpg"
    #         } ,
    #         "physical_attributes": {
    #         "skincolor": "brown",
    #         "haircolor": "black",
    #         "hairstyle": "hair1.jpg",
    #         },
    #         "alpemons": [
    #             {
    #                 "name": "Alpemon1",
    #                 "type": "Fire",
    #                 "XP": 5, #level
    #                 "HP": 20,
    #                 "strength": 15,
    #                 "defense": 10,
    #                 "skills": ["Flame Thrower", "Heat Wave"]
    #             },
    #             {
    #                 "name": "Alpemon2",
    #                 "type": "Water",
    #                 "XP": 3, #level
    #                 "HP": 25,
    #                 "strength": 10,
    #                 "defense": 15,
    #                 "skills": ["Water Gun", "Bubble Beam"]
    #             }
    #         ]
    #         ,
    #         "inventory": 
    #             [{
    #                 "item_id": 1,
    #                 "item_name": "Health Potion",
    #                 "quantity": 5,
    #                 "description": "Restores 20 HP"
    #             },
    #             {
    #                 "item_id": 2,
    #                 "item_name": "Mana Potion",
    #                 "quantity": 3,
    #                 "description": "Restores 15 MP"
    #             },
    #             {
    #                 "item_id": 3,
    #                 "item_name": "Revive",
    #                 "quantity": 1,
    #                 "description": "Revives a fainted Alpemon with half HP"
    #             },
    #             {
    #                 "item_id": 4,  
    #                 "item_name": "Golden Alpemon Ball",
    #                 "quantity": 2,
    #                 "description": "Increases the chance of capturing rare Alpemons"    
    #             }
    #         ]
    #     }
    # )
    # players.insert_one(
    #     {
    #         "name": "Player2",
    #         # outfit and physical attributes as an avatar object
    #         "outfit": {
    #             "hat": "hat2.jpg",
    #             "shirt" : "shirt2.jpg",
    #             "pants": "pants2.jpg",
    #             "accessory": "glasses2.jpg",
    #             "shoes": "shoes2.jpg"
    #         } ,
    #         "physical_attributes": {
    #         "skincolor": "light",
    #         "haircolor": "blonde",
    #         "hairstyle": "hair2.jpg",
    #         },
    #         "alpemons": [
    #             {
    #                 "name": "Alpemon3",
    #                 "type": "Grass",
    #                 "XP": 4, #level
    #                 "HP": 22,
    #                 "strength": 12,
    #                 "defense": 14,
    #                 "skills": ["Vine Whip", "Leaf Blade"]
    #             },
    #             {
    #                 "name": "Alpemon4",
    #                 "type": "Electric",
    #                 "XP": 6, #level
    #                 "HP": 18,
    #                 "strength": 18,
    #                 "defense": 8,
    #                 "skills": ["Thunder Shock", "Electro Ball"]
    #             },
    #             {
    #                 "name": "Alpemon5",
    #                 "type": "Fire",
    #                 "XP": 2, #level
    #                 "HP": 30,
    #                 "strength": 8,
    #                 "defense": 20,
    #                 "skills": ["Ember", "Flame Wheel"]
    #             }
            
    #         ],
    #         "inventory": 
    #             [{
    #                 "item_id": 1,
    #                 "item_name": "Health Potion",
    #                 "quantity": 4,
    #                 "description": "Restores 20 HP"
    #             },
    #             {
    #                 "item_id": 2,
    #                 "item_name": "Mana Potion",
    #                 "quantity": 6,
    #                 "description": "Restores 15 MP"
    #             },
    #             {
    #                 "item_id": 3,
    #                 "item_name": "Revive",
    #                 "quantity": 2,
    #                 "description": "Revives a fainted Alpemon with half HP"
    #             },
    #             {
    #                 "item_id": 4,  
    #                 "item_name": "Silver Alpemon Ball",
    #                 "quantity": 5,
    #                 "description": "Increases the chance of capturing uncommon Alpemons"    
    #             }
    #         ]  
    #     }
    # )
    # print("Database connected successfully:", database)
    fire_alpemons = get_alpemons_by_type("Player2", "Fire")
    print("Fire Alpemons for Player2 (aggregation):", fire_alpemons, "qty:", fire_alpemons.countDocuments())
    
    
    #lets insert a new fire alpemon for Player2
    players.update_one(
        {"name": "Player2"},
        {"$push": {
            "alpemons": {
                "name": "Alpemon6",
                "type": "Fire",
                "XP": 1,
                "HP": 28,
                "strength": 9,
                "defense": 18,
                "skills": ["Flare Blitz", "Fire Spin"]
            }
        }}
    )
    fire_alpemons_p2 = get_alpemons_by_type("Player2", "Fire")
    print("Fire Alpemons for Player2 after adding a new one (aggregation):", fire_alpemons_p2, "qty:", fire_alpemons_p2.countDocuments())
    
except Exception as e:
    print("Error connecting to database:", e)