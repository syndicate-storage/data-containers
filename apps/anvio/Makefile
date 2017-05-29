DATASET_NAME ?= 
BUILD_FLAG ?=

IMAGE_NAME = $(DATASET_NAME)-anvio
DOCKERFILE = ./Dockerfile

.PHONY: all build

all: build

build:
	sed "s/%%BASE_IMAGE%%/$(DATASET_NAME)-syndicate/" Dockerfile.template > Dockerfile
	@docker inspect -f '{{.Id}}' $(IMAGE_NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build $(BUILD_FLAG) -f $(DOCKERFILE) -t $(IMAGE_NAME) . ; fi

push: build
	docker tag $(IMAGE_NAME) syndicatestorage/$(IMAGE_NAME)
	docker push syndicatestorage/$(IMAGE_NAME)
