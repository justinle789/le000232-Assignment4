1.Build Image
	docker image build -t flask_docker .

2.Run the container
	docker run -p 5000:5000 -d flask_docker

3.Log in on your local machine
	docker login

4.Rename the Docker image
	docker tag flask_docker <your-docker-hub-username>/flask-docker

5.Push to Docker Hub
	docker push <your-docker-hub-username>/flask-docker

6.heroku login

7. docker login --username=<your-username> --password=<your-password>

8.heroku create <app-name>

heroku container:login

9.heroku container:push web --app <app-name>

10.heroku container:release web --app <app-name>
