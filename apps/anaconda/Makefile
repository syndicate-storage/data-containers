BUILD_FLAG ?=
IMAGE_NAME = syndicate-anaconda
DOCKERFILE = ./Dockerfile

.PHONY: all build run push

all: run

build:
	@docker inspect -f '{{.Id}}' $(IMAGE_NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build $(BUILD_FLAG) -f $(DOCKERFILE) -t $(IMAGE_NAME) . ; fi

run: build
	@docker run -ti --cap-add SYS_ADMIN --device /dev/fuse --privileged $(IMAGE_NAME)

push: build
	docker tag $(IMAGE_NAME) syndicatestorage/$(IMAGE_NAME)
	docker push syndicatestorage/$(IMAGE_NAME)
