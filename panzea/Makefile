MS_URL ?= demo1.opencloud.cs.arizona.edu:28080
USER_NAME ?= dc_anonymous_user@opencloud.us
VOLUME_NAME ?= panzea
GATEWAY_NAME ?= panzea_anonymous
DATASET_NAME ?= panzea

DOCKER_ARGS = --build-arg MS_URL=$(MS_URL) --build-arg USER_NAME=$(USER_NAME) --build-arg VOLUME_NAME=$(VOLUME_NAME) --build-arg GATEWAY_NAME=$(GATEWAY_NAME) --build-arg DATASET_NAME=$(DATASET_NAME)
BUILD_FLAG ?=

IMAGE_NAME = $(DATASET_NAME)-syndicate
DOCKERFILE = ../datasets/Dockerfile

.PHONY: all build run push

all: run

build:
	-@mkdir ../datasets/cert/
	@cp $(USER_NAME).pkey ../datasets/cert/
	@docker inspect -f '{{.Id}}' $(IMAGE_NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build $(BUILD_FLAG) -f $(DOCKERFILE) -t $(IMAGE_NAME) $(DOCKER_ARGS) ../datasets ; fi
	-@rm -rf ../datasets/cert

build_apps:
	$(MAKE) -C ../apps build DATASET_NAME=$(DATASET_NAME) BUILD_FLAG=$(BUILD_FLAG)

run: build
	@docker run -ti --cap-add SYS_ADMIN --device /dev/fuse --privileged $(IMAGE_NAME)

push: build
	docker tag $(IMAGE_NAME) syndicatestorage/$(IMAGE_NAME)
	docker push syndicatestorage/$(IMAGE_NAME)

push_apps:
	$(MAKE) -C ../apps push DATASET_NAME=$(DATASET_NAME) BUILD_FLAG=$(BUILD_FLAG)
