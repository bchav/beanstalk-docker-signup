# Beanstalk Docker demo repo

Source files for spinning up a Docker application on AWS Elastic Beanstalk, based on https://github.com/awslabs/eb-py-flask-signup

The application is a "Sign Up" application for "A New Startup". The application inserts names and email addresses into Redis.

The architecture is an Nginx container acting as a transpartent reverse proxy. It is linked to the app.py container using the "links" parameter in the Dockerrun.aws.json file. The Nginx source repo is here: https://github.com/bchav/nginx-proxy

To get this up and running:

1. Clone the repo and cd into the directory.
2. Edit app.py to point to a redis server.
3. Build a container by running `docker build -t . repo/image-name:version`
4. Push the container image into a repository
5. Edit dockerrun.aws.json to point to your containers image
6. [Deploy a Beanstalk env](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_v2config.html) with the dockerrun.aws.json file
