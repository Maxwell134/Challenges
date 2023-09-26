from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound



# Create your views here.

# Existing authors and books (from the previous list)
authors = {
    "J.K. Rowling": ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets",
                     "Harry Potter and the Prisoner of Azkaban"],
    "George R.R. Martin": ["A Game of Thrones", "A Clash of Kings", "A Storm of Swords"],
    "Agatha Christie": ["Murder on the Orient Express", "The Murder of Roger Ackroyd", "Death on the Nile"],
    "Stephen King": ["The Shining", "It", "Carrie"],
    "Jane Austen": ["Pride and Prejudice", "Sense and Sensibility", "Emma"],
    "William Shakespeare": ["Hamlet", "Romeo and Juliet", "Macbeth"],
    "Mark Twain": ["The Adventures of Huckleberry Finn", "The Adventures of Tom Sawyer"],
    "Leo Tolstoy": ["War and Peace", "Anna Karenina", "The Death of Ivan Ilyich"],
    "F. Scott Fitzgerald": ["The Great Gatsby", "Tender Is the Night", "This Side of Paradise"],
    "Emily Brontë": ["Wuthering Heights"],
    "Haruki Murakami": ["Norwegian Wood", "Kafka on the Shore", "1Q84"],
    "Margaret Atwood": ["The Handmaid's Tale", "Alias Grace", "Oryx and Crake"],
    "Charles Bukowski": ["Post Office", "Ham on Rye", "Women"],
    "Gabriel García Márquez": ["One Hundred Years of Solitude", "Love in the Time of Cholera",
                               "Chronicle of a Death Foretold"],
    "Toni Morrison": ["Beloved", "Song of Solomon", "Sula"],
    "Aldous Huxley": ["Brave New World", "Island", "The Doors of Perception"],
    "Fyodor Dostoevsky": ["Crime and Punishment", "The Brothers Karamazov", "The Idiot"],
    "Franz Kafka": ["The Metamorphosis", "The Trial", "The Castle"],
    "Oscar Wilde": ["The Picture of Dorian Gray", "The Importance of Being Earnest", "De Profundis"],
    "Victor Hugo": ["Les Misérables", "The Hunchback of Notre-Dame", "Toilers of the Sea"],
    "Charlotte Brontë": ["Jane Eyre", "Shirley", "Villette"],
    "Thomas Hardy": ["Tess of the d'Urbervilles", "Far from the Madding Crowd", "The Mayor of Casterbridge"],
    "Johann Wolfgang von Goethe": ["Faust", "The Sorrows of Young Werther", "Wilhelm Meister's Apprenticeship"],
    "J.R.R. Tolkien": ["The Lord of the Rings", "The Hobbit", "The Silmarillion"],
    "Isaac Asimov": ["Foundation", "I, Robot", "The Caves of Steel"],
    "Ray Bradbury": ["Fahrenheit 451", "The Martian Chronicles", "Dandelion Wine"],
    "George Orwell": ["1984", "Animal Farm", "Homage to Catalonia"],
    "Ernest Hemingway": ["The Old Man and the Sea", "A Farewell to Arms", "For Whom the Bell Tolls"],
    "H.P. Lovecraft": ["The Call of Cthulhu", "At the Mountains of Madness", "The Shadow over Innsmouth"],
    "Jules Verne": ["Twenty Thousand Leagues Under the Sea", "Journey to the Center of the Earth",
                    "Around the World in Eighty Days"],
    "Louisa May Alcott": ["Little Women", "Little Men", "Jo's Boys"],
    "Arthur Conan Doyle": ["Sherlock Holmes Series", "The Lost World", "The Hound of the Baskervilles"],
    "Virginia Woolf": ["Mrs. Dalloway", "To the Lighthouse", "Orlando"],
    "Harper Lee": ["To Kill a Mockingbird"],
    "Albert Camus": ["The Stranger", "The Myth of Sisyphus"],
    "Homer": ["The Iliad", "The Odyssey"],
    "Mintu" : [],
}

# The dictionary now contains more than 100 authors and their books.


def index(request):

    author_names = list(authors.keys())
    print(author_names)
    return render(request, "index.html", {"author_names": author_names})

def books(request, author):

    if author in authors:
        books_list = authors[author]  # Get the list of books for the specified author
        print(books_list)
        # string_name = randint(2000, 9000)
        return render(request, 'authors.html', {"books_list": books_list, "author_name": author})

    return HttpResponseNotFound("Author not found. Please enter a correct author name.")


def add_book(request, author_name= None, book_title= None):
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        book_title = request.POST.get('book_title')

        if author_name in authors:
            # Add the new book to the author's list of books
            authors[author_name].append(book_title)
            return redirect(reverse('books', args=[author_name]))
        else:
            return HttpResponse("Author not found. Please enter a correct author name.")
    else:
        return render(request, 'add_book.html', {"author_name": author_name, "book_title": book_title})


def search_book(request):
    if request.method == "POST":
        author_name = request.POST.get('author_name')
        book_title = request.POST.get('book_title')

        if author_name in authors:
            book_list = authors[author_name]
            matching_books = [book for book in book_list if book_title.lower() in book.lower()]
            return render(request, 'search_results.html', {"author_name": author_name, "matching_books": matching_books})

    return render(request, 'search.html')


def redirect_to_books(request, author_name):
    if author_name in authors:
        return redirect(reverse('books', args=[author_name]))

def delete_author(request, author):

    if author in authors:
        del authors[author]
        return redirect(reverse('index'))

    else:
        return HttpResponseNotFound("Author not found. Please enter a correct author name.")




