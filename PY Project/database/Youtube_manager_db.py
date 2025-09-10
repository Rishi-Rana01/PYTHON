import sqlite3

conn=sqlite3.connect('Youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')
def list_videos():
    print("\n")
    print("Here is the list of all youtube videos: ")
    print("*" *60)
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    print("\n")
    print("*" *60)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES(?, ?)", (name, time))
    conn.commit()


def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time=? WHERE id = ?",(new_name, new_time,video_id) )
    conn.commit()
    
 
def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?",(video_id,))
    conn.commit()
 

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List all YouTube video")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video  details")
        print("4. Delete a Youtube video")
        print("5. Exit the app")

        choice=input("Enter Your choice : ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name=input("Enter the Video name: ")
            time=input("Enter the Video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id=input("Enter Video ID to update: ")
            name=input("Enter the Video name: ")
            time=input("Enter the Video time: ")
            update_video(video_id,name, time)
        elif choice == '4':
            video_id=input("Enter Video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")
    conn.close()        
if __name__ == "__main__":
    main()