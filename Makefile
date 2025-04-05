
all:
	@echo "Starting up all services..."
	@docker-compose -f ./Devops/docker-compose.yml up --build -d

grafana:
	@echo "Starting up Grafana services..."
	@docker-compose -f ./Devops/Monitoring-System/docker-compose.yml up --build -d

build:
	@docker-compose -f ./Devops/docker-compose.yml up -d --build

grafana_build:
	@docker-compose -f ./Devops/Monitoring-System/docker-compose.yml up -d --build

down:
	@docker-compose -f ./Devops/docker-compose.yml down

grafana_down:
	@docker-compose -f ./Devops/Monitoring-System/docker-compose.yml down

re: down
	@docker-compose -f ./Devops/docker-compose.yml up -d
	@docker-compose -f ./Devops/Monitoring-System/docker-compose.yml up -d

clean: down
	@docker system prune -a

fclean:
	@echo "All data will be deleted! Are you sure (yes/no)"
	@read ans && [ "$$ans" = "yes" ] && \
		docker stop $$(docker ps -qa) && \
		docker system prune --all --force --volumes && \
		docker network prune --force && \
		docker volume prune --force || echo "The operation has been cancelled"

run:
	@if [ "$(RUN_TYPE)" = "grafana" ]; then \
		echo "Running Grafana services..."; \
		docker-compose -f ./Devops/Monitoring-System/docker-compose.yml up --build -d; \
	else \
		echo "Running default services..."; \
		docker-compose -f ./Devops/docker-compose.yml up --build -d; \
	fi

.PHONY : all build down re clean fclean grafana grafana_build grafana_down run
