## **Building and Running the Docker Container**

### **Step 1: Build the Docker Image**

Run the following PowerShell command to build the Docker image:

```powershell
docker build -t library-api .
```

- `-t library-api`: Assigns the name `library-api` to the Docker image.
- `.`: Refers to the current directory where the `Dockerfile` exists.

---

### **Step 2: Run the Docker Container**

Once the image is built, start the container using this PowerShell command:

```powershell
docker run -p 4000:4000 --name library-api-container library-api
```

- `-p 4000:4000`: Maps port 4000 on your computer to port 4000 in the container.
- `--name library-api-container`: Assigns a name to the running container.
- `library-api`: Refers to the Docker image you built.

---

### **Step 3: Verify the API is Running**

After starting the container, verify that the API is running by visiting:

```
http://localhost:4000
```

---

## **Accessing the Swagger API Documentation**

Swagger provides an interactive UI to test and explore the API endpoints.

### **Step 1: Open the Swagger Documentation**

Once the Docker container is running, access the Swagger API documentation by visiting the following route:

```
http://localhost:4000/api-docs
```

---

## **API Endpoints**

The following endpoints are available in the Library Management API:

| **Feature**              | **Method** | **Endpoint**        | **Description**                       |
|--------------------------|------------|---------------------|---------------------------------------|
| Add a new book           | POST       | `/books`            | Adds a new book to the library.       |
| List all books           | GET        | `/books`            | Returns a list of all books.          |
| Search for books         | GET        | `/books?query=...`  | Filters books by author, year, genre. |
| Update book details      | PUT        | `/books/isbn`      | Updates details of a specific book.   |
| Delete a book by ISBN    | DELETE     | `/books/isbn`      | Deletes a specific book by ISBN.      |

- **Base URL**: `http://localhost:4000`

---

## **Example Request**

### Add a New Book (POST `/books`)

**Request Body** (JSON):
```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "publishedYear": 2018,
  "isbn": "333333333",
  "genre": "self-help"
}
```