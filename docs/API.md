# GitHub Analysis API Documentation

## Endpoints

### 1. Health Check
- **GET /**  
  Returns the API status.

### 2. Get Language Statistics
- **GET /api/languages**  
  Returns language statistics stored in MongoDB.

### 3. Run ETL for a GitHub Owner
- **POST /api/etl**  
  Runs the ETL for the specified owner and saves the data in MongoDB.

  **Request Body (JSON):**
  ```json
  {
    "owner": "OWNER_NAME",
    "token": "YOUR_GITHUB_TOKEN"
  }
  ```

  **Response:**
  ```json
  {
    "message": "ETL executed for OWNER_NAME",
    "rows": 42
  }
  ```

### 4. Delete Data for an Owner
- **DELETE /api/etl/<owner>**  
  Deletes all language statistics for the specified owner.

  **Success Response:**
  ```json
  {
    "message": "Data from 'facebook' removed."
  }
  ```

---

## Example usage with curl

```sh
curl -X POST http://localhost:5000/api/etl \
  -H "Content-Type: application/json" \
  -d '{"owner": "facebook", "token": "YOUR_GITHUB_TOKEN"}'
```

---