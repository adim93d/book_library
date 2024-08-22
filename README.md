
# Flask Library Application

## Overview

This is a simple Flask-based library application that allows users to manage books and authors. Users can view a list of books, add new books and authors, and delete books from the library. The application also automatically removes an author if their last book is deleted.

## Features

- **View Books**: The homepage displays a list of all books in the library along with their details, including title, ISBN, author, publication year, and cover photo.
- **Search and Sort**: Users can search for books by title or author and sort the results by book ID, title, or publication year.
- **Add Authors**: A form to add new authors with their name, birth date, and date of death.
- **Add Books**: A form to add new books with details like title, ISBN, publication year, and author.
- **Delete Books**: Users can delete books directly from the homepage. If an author has no other books in the library, the author is also deleted.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure you have Python installed on your system.
- **Flask**: Install Flask via pip.
- **SQLAlchemy**: Install SQLAlchemy via pip.

### Installation

1. **Clone the Repository**:

   \`\`\`bash
   git clone https://github.com/adim93d/book_library.git
   cd library-app
   \`\`\`

2. **Install Dependencies**:

   \`\`\`bash
   pip install flask flask_sqlalchemy
   \`\`\`

3. **Set Up the Database**:

   - The application uses SQLite for the database. To set up the database, uncomment the following lines in \`app.py\` and run the application once to create the necessary tables:

   \`\`\`python
   # Uncomment the lines below to create the database tables if they don't exist
   # with app.app_context():
   #     db.create_all()
   \`\`\`

4. **Run the Application**:

   \`\`\`bash
   python app.py
   \`\`\`

   The application will be available at \`http://localhost:5002\`.

## File Structure

- \`app.py\`: The main application file containing all routes and business logic.
- \`data_models.py\`: Contains the SQLAlchemy models for \`Author\` and \`Book\`.
- \`templates/\`: Contains the HTML templates for the application.
  - \`base.html\`: The base template that includes shared components like the header.
  - \`index.html\`: The homepage template that lists all books.
  - \`add_author.html\`: Template for adding a new author.
  - \`add_book.html\`: Template for adding a new book.

## Usage

### Homepage
- View the list of books.
- Search for books by title or author.
- Sort books by different criteria.
- Delete a book.

### Adding Authors
- Navigate to \`/add_author\` or click the "Add an Author" button on the homepage.
- Fill in the author's name, birth date, and date of death, then submit.

### Adding Books
- Navigate to \`/add_book\` or click the "Add a Book" button on the homepage.
- Select an author from the dropdown and fill in the book details, then submit.

### Deleting Books
- On the homepage, click the "Delete Book" button next to the book you want to delete.
- Confirm the deletion in the prompt.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you find a bug or have a feature request.

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
