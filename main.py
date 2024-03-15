from sensor.configuration.mongo_db_connection import MongoDBClient


#Code to test mongodb connection
if __name__ == '__main__':
    mongodb_client=MongoDBClient()
    print(mongodb_client.database.list_collection_names())