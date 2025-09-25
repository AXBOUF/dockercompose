
# Portfolio Sign-Up Web App

A simple Python web application to collect and display email sign-ups, backed by PostgreSQL, running in Docker containers.

---

## Project Description

This project is a small web application that allows users to sign up with their email. Submitted emails are stored in a PostgreSQL database. The application is containerized using Docker and orchestrated with Docker Compose.

---

## Project Structure

```

web/
├── templates/
│   └── index.html      # Sign-up page
├── app.py              # Python app talking to DB
Dockerfile              # Container setup for web app
docker-compose.yml      # Compose file to manage web + postgres containers
requirements.txt        # Python dependencies

````

---

## Features

- Sign up via email form
- Store emails in PostgreSQL database
- View all signed-up emails
- Data persistence using Docker volumes
- Easy setup using Docker Compose

---

## Technologies

- Python (Flask)
- PostgreSQL
- Docker & Docker Compose
- HTML/CSS (templates)

---

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Run the project

1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
````

2. Build and start containers

```bash
docker-compose up --build
```

3. Open the app in your browser

```
http://localhost:5000
```

4. Stop containers

```bash
docker-compose down
```

---

## Testing Data Persistence

The PostgreSQL data persists even after stopping and restarting containers thanks to Docker volumes.

To verify:

```bash
docker-compose exec -T postgres_container_name psql -U postgres -d mydb
```

Then query:

```sql
SELECT * FROM visitors;
```

---

## Screenshots (Optional)

*Add screenshots of your app here with captions if you like.*

---

## License

MIT License

```

This version will render correctly on GitHub, with proper code blocks and headings.  

If you want, I can also **enhance it with badges, Docker build status, and contribution guidelines** to make it look like a professional portfolio README.  

Do you want me to do that next?
```
