const express = require("express");
const fs = require("fs");
const router = express.Router();

const dataFile = "./data/books.json";

// Helper function to read and write JSON
const readBooks = () => JSON.parse(fs.readFileSync(dataFile));
const writeBooks = (data) => fs.writeFileSync(dataFile, JSON.stringify(data, null, 2));

// 1. Add a new book
router.post("/", (req, res) => {
  const { title, author, publishedYear, isbn, genre } = req.body;
  if (!title || !author || !publishedYear || !isbn) {
    return res.status(400).json({ message: "Missing required fields." });
  }

  const books = readBooks();
  books.push({ title, author, publishedYear, isbn, genre });
  writeBooks(books);

  res.status(201).json({ message: "Book added successfully." });
});

// 2. List all books
router.get("/", (req, res) => {
  const books = readBooks();
  res.json(books);
});

// 3. Search for books
router.get("/search", (req, res) => {
  const { author, publishedYear, genre } = req.query;
  const books = readBooks();

  const filteredBooks = books.filter((book) => {
    return (
      (book.author === author) ||
      (book.publishedYear == publishedYear) ||
      (book.genre === genre)
    );
  });

  res.json(filteredBooks);
});

// 4. Delete a book by ISBN
router.delete("/:isbn", (req, res) => {
  const { isbn } = req.params;
  let books = readBooks();

  const updatedBooks = books.filter((book) => book.isbn !== isbn);
  if (books.length === updatedBooks.length) {
    return res.status(404).json({ message: "Book not found." });
  }

  writeBooks(updatedBooks);
  res.json({ message: "Book deleted successfully." });
});

// 5. Update book details by ISBN
router.put("/:isbn", (req, res) => {
  const { isbn } = req.params;
  const { title, author, publishedYear, genre } = req.body;

  let books = readBooks();
  const bookIndex = books.findIndex((book) => book.isbn === isbn);

  if (bookIndex === -1) {
    return res.status(404).json({ message: "Book not found." });
  }

  books[bookIndex] = { ...books[bookIndex], title, author, publishedYear, genre };
  writeBooks(books);

  res.json({ message: "Book updated successfully." });
});

module.exports = router;
