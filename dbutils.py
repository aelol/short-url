import pymongo

client = pymongo.MongoClient('112.74.83.185', 27015)

# client = pymongo.MongoClient('mongodb://root:edydadmin@localhost:27017/')

db = client['short']

# db.authenticate('short', 'edydadmin')

short_collection = db['short_collections']


def save_short(short, raw, update_time):
    post = {
        "short": short,
        "raw": raw,
        "last_update": update_time,
    }

    return short_collection.insert(post)


def usr_update_time(raw):
    return short_collection.find_one({"raw": raw}, {"last_update": 1, "_id": 0})


def usr_total_call(raw):
    return short_collection.find_one({"raw": raw}, {"total_call": 1, "_id": 0})


def find_update_short(short, raw, update_time):
    post = {
        "short": short,
        "raw": raw,
        "last_update": update_time,
    }
    return short_collection.find_one_and_update({"raw": raw}, {'$set':post}, return_document=pymongo.ReturnDocument.AFTER)


def redirect(short):
    data = short_collection.find_one({"short": short}, {"_id": 0})
    return data





