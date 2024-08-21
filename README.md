
# Real Estate Backend Service

## Introduction

Habi aims to provide a tool where users can view available properties for sale. Users should be able to see both sold and available properties, and they should be able to filter the search results based on different criteria. Additionally, users should be able to "like" properties, which will help in ranking the most attractive properties internally.

## Technologies

- **Python 3.9**: The programming language used for developing the backend service.
- **MySQL**: The database for storing and managing data.
- **Docker**: For containerizing the application.

## Project Structure

```
property_service/
├── Dockerfile
├── docker-compose.yml
├── app/
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   └── routes.py
├── requirements.txt
├── main.py
└── tests/
    └── test_routes.py
```

### Dockerfile

Sets up the Python environment, installs dependencies, and runs the application.

### docker-compose.yml

Defines Docker services for the application and MySQL database, including environment variables and service links.
**.env**

The .env file contains environment variables used by the Docker containers. This file is crucial for configuring the application’s connection settings and other environment-specific configurations. Here is an example of the .env file:
   ```bash
        # Database connection settings
      DATABASE_HOST=localhost
      DATABASE_PORT=6033
      DATABASE_USER=habi_user
      DATABASE_PASSWORD=habi_password
      DATABASE_NAME=habi_db
   ```

### app/

Contains the main application code:
- **config.py**: Configuration settings for the application.
- **database.py**: Functions for managing database connections.
- **models.py**: Definitions of database models.
- **routes.py**: API route handlers.

### requirements.txt

Lists the Python dependencies required for the project.

### main.py

The entry point for each microservice, initializing and starting the server for that specific service.

### tests/

Contains unit tests for the application. The `test_routes.py` file includes tests for the API routes.

## Setup and Usage

1. **Build and Run the Docker Containers**

   ```bash
   docker-compose build
   docker-compose up
   ```

2. **Access the Application**

   - The application will be available at `http://localhost:8000`.

3. **Run Tests**

   - To run the tests, use:

     ```bash
     docker-compose up property-service-test
     ```

4. **Stop and Remove Containers**

   ```bash
   docker-compose down
   ```

5. **Run Specific Service**

   ```bash
   docker-compose up property-service-test
   ```

## Explanation of the `property_likes` Table

The `property_likes` table tracks which users have liked which properties. It includes:

- `id`: Unique identifier for the like record.
- `property_id`: Foreign key linking to the `property` table.
- `user_id`: Foreign key linking to the `auth_user` table.
- `created_at`: Timestamp when the like was created.

This setup allows tracking of user interactions with properties and enables ranking based on user preferences.

## Possible Improvements

### Using Redis for Caching

**Benefits:**
- **Faster Data Access:** Stores frequently accessed data in memory for quicker retrieval.
- **Reduced Database Load:** Decreases the number of queries to the database.
- **Improved Performance:** Enhances user experience with faster response times.

**Implementation:**
1. Integrate Redis with the application.
2. Cache frequently accessed data to reduce load on the database.

### Adopting a Microservices Architecture with AWS Lambda

**Benefits:**
- **Scalability:** AWS Lambda scales automatically with demand.
- **Cost Efficiency:** Pay only for the compute time used.
- **Flexibility:** Each service runs independently, allowing for easier updates and management.

**Implementation:**
1. Decompose the application into microservices.
2. Deploy each service as an AWS Lambda function for better scalability and cost management.
