
README
This Django project contains views for managing a list of authors and their books. The project includes the following views:

index: Displays a list of all author names.
books: Displays a list of books by a specific author.
add_book: Allows users to add a new book to an existing author's list of books.
search_book: Allows users to search for a book by title within an author's list of books.
redirect_to_books: Redirects to the books view for a specific author.
delete_author: Deletes an author and their list of books from the database.
The authors dictionary contains a list of authors as keys and their corresponding books as values. The dictionary is pre-populated with more than 100 authors and their books.

Running the Project
To run the project locally, follow these steps:

Make sure you have Django installed.
Clone the repository and navigate to the project directory.
Run the Django development server using the command python manage.py runserver.
Access the views in a web browser using the appropriate URLs.
Docker Integration
To run the project using Docker, follow these steps:

Create a Dockerfile in the root directory of your Django project with the provided content.
Create a requirements.txt file with the required Python packages.
Build the Docker image using docker build -t my-django-app ..
Run the Docker container with docker run -p 8000:8000 my-django-app.
Access your Django application in a web browser by visiting http://localhost:8000.
Feel free to explore and modify the code as needed for your project requirements.
