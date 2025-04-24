import json
import requests
import random

#ex-1
with open("books.json", mode="r") as file:
    a=json.load(file)
    for i in a["books"]:
        for el in i:
            print(f"{el}: {i[el]}")
        print("")

#ex-2
url="http://api.openweathermap.org/data/2.5/weather?lat=41.3123363&lon=69.2787079&appid=4c64ec380eda4ba57ee01de480f290b4&units=metric"
try:
    data = requests.get( url , verify=False)
    json_data = data.json()
except:
    print("Internet Ishlamayapti!")
print(f"City: {json_data['name']} \nTemp: {json_data['main']['temp']} \nHumidity: {json_data['main']['humidity']}")

#ex-3

def load_books(filename="books.json"):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def save_books(data, filename="books.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

def display_books(data):
    for book in data["books"]:
        print(f"\nID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Year: {book['publication_year']}")
        print(f"Genre: {', '.join(book['genre'])}")
        print(f"Publisher: {book['publisher']}")
        print(f"ISBN: {book['isbn']}")
        print("-" * 40)

def add_book(data):
    new_book = {
        "id": int(input("Enter ID: ")),
        "title": input("Enter title: "),
        "author": input("Enter author: "),
        "publication_year": int(input("Enter publication year: ")),
        "genre": input("Enter genre(s), separated by commas: ").split(","),
        "publisher": input("Enter publisher: "),
        "isbn": input("Enter ISBN: ")
    }
    new_book["genre"] = [g.strip() for g in new_book["genre"]]
    data["books"].append(new_book)
    print("Book added successfully.")

def update_book(data):
    book_id = int(input("Enter the ID of the book to update: "))
    for book in data["books"]:
        if book["id"] == book_id:
            book["title"] = input("Enter new title: ")
            book["author"] = input("Enter new author: ")
            book["publication_year"] = int(input("Enter new publication year: "))
            book["genre"] = input("Enter new genre(s), separated by commas: ").split(",")
            book["genre"] = [g.strip() for g in book["genre"]]
            book["publisher"] = input("Enter new publisher: ")
            book["isbn"] = input("Enter new ISBN: ")
            print("Book updated successfully.")
            return
    print("Book not found.")

def delete_book(data):
    book_id = int(input("Enter the ID of the book to delete: "))
    for i, book in enumerate(data["books"]):
        if book["id"] == book_id:
            del data["books"][i]
            print("Book deleted successfully.")
            return
    print("Book not found.")

def main():
    books_data = load_books()

    while True:
        print("\n=== Book Manager ===")
        print("1. Display all books")
        print("2. Add a new book")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            display_books(books_data)
        elif choice == "2":
            add_book(books_data)
        elif choice == "3":
            update_book(books_data)
        elif choice == "4":
            delete_book(books_data)
        elif choice == "5":
            save_books(books_data)
            print("Changes saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#ex-4
API_KEY = "83e0c398"
BASE_URL = "http://www.omdbapi.com/"

def get_movies_by_keyword(keyword):
    url = f"{BASE_URL}?s={keyword}&apikey={API_KEY}"
    try:
        response = requests.get(url, verify=False)
        data = response.json()
        return data.get("Search", [])
    except:
        print("Internet ishlamayapti!")
        return []

def get_movie_details(imdb_id):
    url = f"{BASE_URL}?i={imdb_id}&apikey={API_KEY}"
    try:
        response = requests.get(url, verify=False)
        return response.json()
    except:
        return None

def recommend_random_movie(genre_keyword):
    movies = get_movies_by_keyword(genre_keyword)
    if not movies:
        print("No movies found for this keyword.")
        return

    random_movie = random.choice(movies)
    details = get_movie_details(random_movie["imdbID"])

    if details:
        print("\n🎬 Recommended Movie:")
        print(f"Title: {details['Title']}")
        print(f"Year: {details['Year']}")
        print(f"Genre: {details['Genre']}")
        print(f"Plot: {details['Plot']}")
        print(f"IMDB Rating: {details['imdbRating']}")
    else:
        print("Could not fetch movie details.")
user_input = input("Enter a movie genre or keyword (e.g. Action, Comedy, Romance): ")
recommend_random_movie(user_input)




