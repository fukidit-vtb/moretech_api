docker_build:
	docker build -t aleontiev/vtb_api:last -f ./Dockerfile .

docker_push:
	docker push aleontiev/vtb_api:last

dc_up:
	docker-compose up -d

dc_down:
	docker-compose down

dc_build:
	docker-compose build

dc_logs:
	docker-compose logs -f

