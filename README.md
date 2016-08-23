# Beanstalk Docker demo repo

Source files for spinning up a basic docker application on beanstalk.

The application is a "signup" application that inserts values into Redis.

The demo uses an Nginx transparent reverse proxy container linked to the app.py container.

To get this up and running:

1. Clone the repo and cd into the directory.
2. Edit app.py to point to a redis server.
3. Build a container by running `docker build -t . repo/image-name:version`
4. Push the container image into a repository
5. Edit dockerrun.aws.json to point to your containers image
6. [Deploy a Beanstalk env](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker_v2config.html) with the dockerrun.aws.json file
