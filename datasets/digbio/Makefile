APP_NAME ?= base
IMAGE_BASE ?= sdm-$(APP_NAME)
DATASET_NAME ?= digbio

DOCKER_ARGS = --build-arg DATASET_NAME=$(DATASET_NAME)
BUILD_FLAG ?= --squash

IMAGE_NAME = $(DATASET_NAME)-$(APP_NAME)
DOCKERTEMPLATEFILE = ../Dockerfile.template
DOCKERFILE = ../Dockerfile

.PHONY: all clean build rebuild run push repush

all: run

sed:
	@sed "s/%%IMAGE_BASE%%/$(IMAGE_BASE)/" $(DOCKERTEMPLATEFILE) > $(DOCKERFILE)

clean:
	@CONTAINERS="$(shell docker ps -a -q --filter=ancestor=$(IMAGE_NAME) | awk '{print $$1}')" ; if [ ! -z "$$CONTAINERS" ] ; then docker rm $$CONTAINERS ; fi
	@docker inspect -f '{{.Id}}' syndicatestorage/$(IMAGE_NAME) 2> /dev/null ; if [ $$? -eq 0 ] ; then docker rmi -f syndicatestorage/$(IMAGE_NAME) ; fi
	@docker inspect -f '{{.Id}}' $(IMAGE_NAME) 2> /dev/null ; if [ $$? -eq 0 ] ; then docker rmi -f $(IMAGE_NAME) ; fi
	@DANGLINGS="$(shell docker images -f "dangling=true" -q)" ; if [ ! -z "$$DANGLINGS" ] ; then docker rmi $$DANGLINGS ; fi

build: sed
	@docker inspect -f '{{.Id}}' $(IMAGE_NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build $(BUILD_FLAG) -f $(DOCKERFILE) -t $(IMAGE_NAME) $(DOCKER_ARGS) .. ; fi
	@docker tag $(IMAGE_NAME) syndicatestorage/$(IMAGE_NAME)

rebuild: clean build
	

run: build
	@docker run -ti --privileged $(IMAGE_NAME)

push: build
	@docker push syndicatestorage/$(IMAGE_NAME)

repush: clean push
	
