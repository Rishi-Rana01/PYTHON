
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("Here is the list of all youtube videos: ")
    print("*" *60)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video ['name']}, Duration: {video['time']}") 
    print("\n")
    print("*" *60)

def add_video(videos):
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos= load_data()
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all YouTube video")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video  details")
        print("4. Delete a Youtube video")
        print("5. Exit the app")

        choice=input("Enter Your choice : ")
        # print(videos)

        match choice:
            case "1":
                list_all_videos(videos)

            case "2":
                add_video(videos)

            case "3":
                update_video(videos)

            case "4":
                delete_video(videos)
            
            case "5":
                break

            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()