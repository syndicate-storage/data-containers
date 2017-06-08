BUILD_FLAG ?=
IMAGE_NAME = syndicate-jupyter
DOCKERFILE = ./Dockerfile

.PHONY: all build run push

all: run

build:
	@docker inspect -f '{{.Id}}' $(IMAGE_NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build $(BUILD_FLAG) -f $(DOCKERFILE) -t $(IMAGE_NAME) . ; fi
	docker tag $(IMAGE_NAME) syndicatestorage/$(IMAGE_NAME)

run: build
	@docker run -ti --cap-add SYS_ADMIN --device /dev/fuse --privileged -p 8888:8888 $(IMAGE_NAME)

push: build
	docker push syndicatestorage/$(IMAGE_NAME)
