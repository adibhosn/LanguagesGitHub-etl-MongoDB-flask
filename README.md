# GitHub Analysis

A Flask REST API for extracting, processing, and analyzing programming language statistics from public GitHub repositories. Data is stored in MongoDB and all services run easily with Docker Compose.

---

## Features

- Run ETL (Extract, Transform, Load) for any GitHub user/organization by sending a POST request with their username and your GitHub token.
- Store and query language statistics for any owner in MongoDB.
- Delete language statistics for a specific owner.
- All endpoints documented and easy to use.
- No need to install MongoDB locally—everything runs in Docker.

---

## Quickstart

### 1. Clone the repository

```sh
git clone https://github.com/your-username/github-analysis.git
cd github-analysis
```

### 2. Configure environment variables

Create a `.env` file in the project root (or use the provided `.env.example`):

```
MONGO_URI=mongodb://mongodb:27017/
```

> **Note:** You do **not** need to add your GitHub token to `.env`. The token is sent in each POST request.

### 3. Build and run with Docker Compose

```sh
docker-compose -f infra/docker/docker-compose.yml up --build
```

This will start both the Flask API and MongoDB.

---

## API Documentation

See [`docs/API.md`](docs/API.md) for full endpoint documentation.

### Main Endpoints

#### Health Check

```
GET /
```

#### Get Language Statistics

```
GET /api/languages
```

#### Run ETL for a GitHub Owner

```
POST /api/etl
```

**Request Body:**
```json
{
  "owner": "OWNER_NAME",
  "token": "YOUR_GITHUB_TOKEN"
}
```

#### Delete Data for an Owner

```
DELETE /api/etl/<owner>
```

---

## Example Usage

**Run ETL for Facebook:**
```sh
curl -X POST http://localhost:5000/api/etl \
  -H "Content-Type: application/json" \
  -d '{"owner": "facebook", "token": "YOUR_GITHUB_TOKEN"}'
```

**Get all language statistics:**
```sh
curl http://localhost:5000/api/languages
```

**Delete statistics for an owner:**
```sh
curl -X DELETE http://localhost:5000/api/etl/facebook
```

---

## Architecture

- **Flask API**: Handles HTTP requests and orchestrates ETL.
- **ETL Service**: Fetches and processes data from GitHub.
- **MongoDB**: Stores repositories and language statistics.
- **Docker Compose**: Orchestrates containers for API and MongoDB.

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for more details.

---

## Deployment

For local use, Docker Compose is all you need.

For production (e.g., AWS ECS, EC2, or Elastic Beanstalk):
- Build and push your Docker images to a registry (like Amazon ECR).
- Deploy using your preferred AWS service.
- Use MongoDB Atlas or a managed MongoDB for production.

**Never commit secrets or AWS credentials to your repository.**

---

## License

MIT License

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---