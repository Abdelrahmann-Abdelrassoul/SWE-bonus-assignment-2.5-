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
docker run -p 3000:3000 --name library-api-container library-api
```

- `-p 3000:3000`: Maps port 3000 on your computer to port 3000 in the container.
- `--name library-api-container`: Assigns a name to the running container.
- `library-api`: Refers to the Docker image you built.

---

### **Step 3: Verify the API is Running**

After starting the container, verify that the API is running by visiting:

```
http://localhost:3000
```

---

## **Accessing the Swagger API Documentation**

Swagger provides an interactive UI to test and explore the API endpoints.

### **Step 1: Open the Swagger Documentation**

Once the Docker container is running, access the Swagger API documentation by visiting the following route:

```
http://localhost:3000/api-docs
```

---

## **API Endpoints**

The following endpoints are available in the Library Management API:

| **Feature**              | **Method** | **Endpoint**        | **Description**                       |
|--------------------------|------------|---------------------|---------------------------------------|
| Add a new book           | POST       | `/books`            | Adds a new book to the library.       |
| List all books           | GET        | `/books`            | Returns a list of all books.          |
| Search for books         | GET        | `/books?query=...`  | Filters books by author, year, genre. |
| Update book details      | PUT        | `/books/:isbn`      | Updates details of a specific book.   |
| Delete a book by ISBN    | DELETE     | `/books/:isbn`      | Deletes a specific book by ISBN.      |

- **Base URL**: `http://localhost:3000`

---

## **Example Requests**

### Add a New Book (POST `/books`)

**Request Body** (JSON):
```json
{
  "title": "Sample Book",
  "author": "John Doe",
  "publishedYear": 2023,
  "isbn": "123-4567890123",
  "genre": "Fiction"
}
```

### Search Books (GET `http://localhost:3000/books/James-Clear`)

**Request**:
```
http://localhost:3000/books/James-Clear
```

---

## **Stopping and Restarting the Container**

### Stop the Container
To stop the running Docker container, use the following PowerShell command:

```powershell
docker stop library-api-container
```

---

### Restart the Container
To restart the container, run:

```powershell
docker start library-api-container
```

---

### Remove the Container
If you want to remove the container completely, run:

```powershell
docker rm library-api-container
```

---

## **Troubleshooting**

### Port Conflict (EADDRINUSE)
If port 3000 is already in use, you can run the container on a different port:

```powershell
docker run -p 4000:3000 --name library-api-container library-api
```

Now the API will be accessible at `http://localhost:4000`.

### Check Docker Logs
To view logs from the running Docker container:

```powershell
docker logs library-api-container
```

---

## **Conclusion**

By following these instructions, you can:
1. Build and run the Library Management API using Docker.
2. Access the interactive Swagger documentation to test endpoints.

Feel free to contribute or report any issues to improve this project!