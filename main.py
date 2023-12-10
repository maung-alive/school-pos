from database import mongo_connect, get_database

from student import Student
from teacher import Teacher

def main():
    client = mongo_connect()
    db = get_database(client, "school")

if __name__ == "__main__":
    main()