## Docker Intro App

This repo contains a minimal working example of a small application running as a collection of docker containers. The aim is to demonstrate the primary docker concepts (ie, images, containers, networks). 

This application consists of 3 containers: a FastAPI api, a Streamlit UI, and a postgres database backend. 

### Getting started

Clone this repository

```
git clone https://github.com/mwhalen-shamrock/stc-ml-docker-intro.git
```

Launch the services

```
docker compose up --build
```

Access the streamlit UI on your local machine via `http://localhost:8501`.

Access the API Swagger documentation via `http://localhost:8000/docs`

