## Docker Intro App

This repo contains a minimal working example of a small application running as a collection of docker containers. The aim is to demonstrate the primary docker concepts (ie, images, containers, networks). 

This application consists of 3 containers: a FastAPI api, a Streamlit UI, and a postgres database backend. 

While this application is intentionally simplistic it can be easily extended to include additional services or extend the endpoint capabilities.

### Getting started

Clone this repository

```
git clone https://github.com/mwhalen-shamrock/stc-ml-docker-intro.git
```

Launch the services

```
docker compose up --build
```

Access the streamlit UI on your local machine via [http://localhost:8501](http://localhost:8501). Test the prediction endpoint by clicking the `Call the API` button. Test the API --> Database connectivity with a simple query `SELECT 1 as foo;` and click `Query the database`.

Access the API Swagger documentation via [http://localhost:8000/docs](http://localhost:8000/docs)

