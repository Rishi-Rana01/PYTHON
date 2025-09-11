from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://Project:Project123@cluster0.issqpkr.mongodb.net/", tls=True, tlsAllowInvalidCertificates=True)
db = client['Youtube_manager']
video_collection = db['videos']

print(video_collection)

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_videos():
    videos = video_collection.find()
    for video in videos:
        print(f"ID: {video['_id']}, Name: {video['name']}, Duration: {video['time']}")

def update_video(video_id, name, time):
    video_collection.update_one({"_id":ObjectId(video_id)}, {"$set": {"name": name, "time": time}})

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\n YouTube Video Manager")
        
        print("1. View Videos")
        print("2. Add Video")
        print("3. Update Videos")
        print("4. Delete Video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time=input("Enter video duration: ")

            add_video(name, time)

        elif choice == '3':
            video_id=input("Enter video ID to update: ")
            name = input("Enter video name: ")
            time=input("Enter video duration: ")

            update_video(video_id, name, time)

        elif choice == '4':
            video_id = input("Enter video ID to delete: ")

            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()