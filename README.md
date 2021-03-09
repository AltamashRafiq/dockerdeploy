# Flask Application - Deployed via Docker

This is a simple Python Flask application containerized using Docker and published on Docker Hub. The app's functionlity is straightforward: given the name of a person via the --name argument, the application returns a hello message addressed to the named person.

# Installation

To download the app to your local machine do the following:

```{bash}
docker pull altamashrafiq/flask-container
```

# Usage

To use the app, replace <name> in the following command with the person you wish to address the message to.

```{bash}
docker run -t altamashrafiq/flask-container python app.py --name <name>
```

# Demo

A demo video for this application can watched here: 

As per the demo, we can run:

```{bash}
docker run -t altamashrafiq/flask-container python app.py --name Ammara
```

which returns: Hello Ammara! This is Altamash :)