
# PyjamaHR Backend Task: Notes

I have successfully completed and tested the given task.




## Tech Stack

**Database:** PostgreSQL (Docker Image)

**Server:** Python/Django




## Hosted API

I have hosted the API on my own server at https://notestask.ujjawal.co/

*Postman collection is also added to the repo.*

**Endpoint:** `/notes/`

**Postman Documentation:** https://documenter.getpostman.com/view/15719295/2s9XxvTuai
## Environment Variables

To start with, you will need to add the following environment variables to your .env file

```bash
URL=notestask.ujjawal.co
PORT=8000
POSTGRES_USER=notes
POSTGRES_PASSWORD=iamsecured
POSTGRES_DB=notes
POSTGRES_HOST=postgres
POSTGRES_PORT=6600
SECRET_KEY=iamsecret
DEBUG=False
```

## Docker

To start the API and Postgres services run

```bash
  docker compose up
```

## TODO

- Logging & Error Handling Middlewares
- Testing CI/CD
- Gunicorn server