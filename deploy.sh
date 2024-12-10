# deploy.sh
docker network create app-network
docker run --name db --network app-network -d dennis213/st:mysql
docker run --name flask-app --network app-network -d -p 5001:5000 dennis213/flask-app
