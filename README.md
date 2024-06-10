# Memes API

Memes API is a Python web application built with FastAPI.

## Features

- **GET /memes**: Get a list of all memes.
- **GET /memes/{id}**: Get a specific meme by its ID.
- **POST /memes**: Add a new meme (with image and text).
- **PUT /memes/{id}**: Update an existing meme.
- **DELETE /memes/{id}**: Delete a meme.

## Requirements

- Docker
- Docker Compose

## Installation and Running

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo/memes-api.git
    cd memes-api
    ```

2. Build and start the containers using Docker Compose:

    ```bash
    docker-compose up --build
    ```

    This command will create and start four services: the memes API, the media file service, a PostgreSQL database, and MinIO storage.

3. Open your browser and go to [http://localhost:8000](http://localhost:8000) to see the welcome message.

4. Swagger documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).

## Testing

To run tests, follow these steps:

1. Ensure the containers are running:

    ```bash
    docker-compose up --build
    ```

2. In another terminal, run the tests:

    ```bash
    docker-compose run test
    ```
