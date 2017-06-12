APP_NAME ?= base
IMAGE_BASE ?= syndicate-$(APP_NAME)
MS_URL ?= http://syndicate-ms-datasets-prod.appspot.com:80
USER_NAME ?= dc_anonymous_user@opencloud.us
VOLUME_NAME ?= imicrobe
GATEWAY_NAME ?= imicrobe_anonymous
DATASET_NAME ?= imicrobe

DOCKER_ARGS = --build-arg MS_URL=$(MS_URL) --build-arg USER_NAME=$(USER_NAME) --build-arg VOLUME_NAME=$(VOLUME_NAME) --build-arg GATEWAY_NAME=$(GATEWAY_NAME) --build-arg DATASET_NAME=$(DATASET_NAME)
BUILD_FLAG ?=

IMAGE_NAME = $(DATASET_NAME)-$(APP_NAME)
DOCKERTEMPLATEFILE = ../Dockerfile.template
DOCKERFILE = ../Dockerfile
CERT_PATH = ../cert

.PHONY: all build run push

all: run

sed:
	echo sed "s/%%IMAGE_BASE%%/$(IMAGE_BASE)/" $(DOCKERTEMPLATEFILE) > $(DOCKERFILE)
	sed "s/%%IMAGE_BASE%%/$(IMAGE_BASE)/" $(DOCKERTEMPLATEFILE) > $(DOCKERFILE)

build: sed
	-@mkdir $(CERT_PATH)
	@cp $(USER_NAME).pkey $(CERT_PATH)
	@docker inspect -f '{{.Id}}' $(IMAGE_NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build $(BUILD_FLAG) -f $(DOCKERFILE) -t $(IMAGE_NAME) $(DOCKER_ARGS) .. ; fi
	-@rm -rf $(CERT_PATH)
	docker tag $(IMAGE_NAME) syndicatestorage/$(IMAGE_NAME)

run: build
	@docker run -ti --cap-add SYS_ADMIN --device /dev/fuse --privileged $(IMAGE_NAME)

push: build
	docker push syndicatestorage/$(IMAGE_NAME)
