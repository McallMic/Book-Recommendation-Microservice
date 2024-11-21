import json
import random
import time


#Book array with genres
BOOKS = [
    #Fiction
    {
        "title": "Tomorrow, and Tomorrow, and Tomorrow",
        "author": "Gabrielle Zevin",
        "genre": "Fiction",
        "goodreads_link": "https://www.goodreads.com/book/show/58784475-tomorrow-and-tomorrow-and-tomorrow",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1636978687i/58784475.jpg"
    },
    {
        "title": "The Seven Husbands of Evelyn Hugo",
        "author": "Taylor Jenkins Reid",
        "genre": "Fiction",
        "goodreads_link": "https://www.goodreads.com/book/show/32620332-the-seven-husbands-of-evelyn-hugo",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1664458761i/32620332.jpg"
    },
    
    #Nonfiction
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "Nonfiction",
        "goodreads_link": "https://www.goodreads.com/book/show/40121378-atomic-habits",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1655988385i/40121378.jpg"
    },
    {
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "genre": "Nonfiction",
        "goodreads_link": "https://www.goodreads.com/book/show/23692271-sapiens",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1595674533i/23692271.jpg"
    },

    #Fantasy
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "goodreads_link": "https://www.goodreads.com/book/show/5907.The_Hobbit",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1546071216i/5907.jpg"
    },
    {
        "title": "The Name of the Wind",
        "author": "Patrick Rothfuss",
        "genre": "Fantasy",
        "goodreads_link": "https://www.goodreads.com/book/show/186074.The_Name_of_the_Wind",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1270352123i/186074.jpg"
    },

    #Science Fiction
    {
        "title": "Project Hail Mary",
        "author": "Andy Weir",
        "genre": "Science Fiction",
        "goodreads_link": "https://www.goodreads.com/book/show/54493401-project-hail-mary",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1597695864i/54493401.jpg"
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Science Fiction",
        "goodreads_link": "https://www.goodreads.com/book/show/44767458-dune",
        "cover_image": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1555447414i/44767458.jpg"
    }
]

def get_book_recommendation(genre=None):
    """Get a random book recommendation, optionally filtered by genre"""
    if genre:
        # Filter books by genre (case-insensitive)
        genre_books = [book for book in BOOKS if book['genre'].lower() == genre.lower()]
        if not genre_books:
            return {"error": f"No books found for genre: {genre}"}
        selected_book = random.choice(genre_books)
    else:
        selected_book = random.choice(BOOKS)
    
    # Write the selected book to a file
    with open('recommended_book.json', 'w') as f:
        json.dump(selected_book, f, indent=2)
    
    return selected_book



if __name__ == "__main__":
   
    print("Book recommendation service is running...")
    print("Monitoring request.txt for genre requests...")
    
    while True:
        try:
            # Read the request file
            with open('request.txt', 'r') as f:
                request = f.read().strip()
            
            # Only process if there's content
            if request:
                # Set genre based on request
                genre = None if request.lower() == "any" else request
                
                # Get and save the recommendation
                book = get_book_recommendation(genre)

                
                # Clear the request file
                with open('request.txt', 'w') as f:
                    f.write('')
            
            # Small delay to prevent excessive CPU usage
            time.sleep(0.1)
            
        except FileNotFoundError:
            # Create request.txt if it doesn't exist
            with open('request.txt', 'w') as f:
                f.write('')
            time.sleep(0.1)