from pymongo import MongoClient

id = "mongodb+srv://mckmarly1101:afpnQhiddfXjdS6U@cluster1101.8fddo05.mongodb.net/cgm_gb?retryWrites=true&w=majority"
# Replace this with your actual connection string

# Replace the following with your MongoDB connection string
# Example: mongodb+srv://<username>:<password>@cluster.mongodb.net/<database>
connection_string = id

# Establish a connection to the MongoDB cluster
client = MongoClient(connection_string)

# Access the desired database
db = client.get_database("cgm_gb")

# Access the desired collection within the database
collection = db["cgm_gb_tes"]

# Create a sample document
new_document = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
}

# Insert the document into the collection
insert_result = collection.insert_one(new_document)

# Print the inserted document's ID
print("Inserted document ID:", insert_result.inserted_id)

# Find and print all documents in the collection
for document in collection.find():
    print(document)

# Close the connection
client.close()



# mckmarly1101
# afpnQhiddfXjdS6U
# mongodb+srv://mckmarly1101:afpnQhiddfXjdS6U@cluster1101.8fddo05.mongodb.net/?retryWrites=true&w=majority

#mongodb+srv://tricia1101:findingnemo1101!@cluster0.noaso.mongodb.net/cgm_gb?retryWrites=true&w=majority