.DEFAULT_GOAL := help

REPO := alesr
IMAGE_NAME := python-exercises

.PHONY: help
help:
	@echo "------------------------------------------------------------------------"
	@echo "Python-exercises"
	@echo "------------------------------------------------------------------------"
	@grep -E '^[a-zA-Z_/%\-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build: ## Build Docker image
	@docker build -t ${REPO}/${IMAGE_NAME} .

run: build ## Run Docker container
	@docker run -ti -d --name ${IMAGE_NAME} ${REPO}/${IMAGE_NAME}

status: ## Output containers
	@docker ps -a

clean: ## Remove previous container
	@./resources/scripts/rm-container.sh ${IMAGE_NAME}

purge: clean ## Remove container AND image
	@./resources/scripts/rm-image.sh ${REPO}/${IMAGE_NAME}

test: clean build run ## Run py.test to test scripts under practice directory
	@docker exec -it ${IMAGE_NAME} \
		py.test --verbose --cov=practice practice

