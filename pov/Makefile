MS_URL ?= demo1.opencloud.cs.arizona.edu:28080
USER_NAME ?= dc_anonymous_user@opencloud.us
VOLUME_NAME ?= pov
GATEWAY_NAME ?= pov_anonymous
DATASET_NAME ?= pov

DOCKER_ARGS = --build-arg MS_URL=$(MS_URL) --build-arg USER_NAME=$(USER_NAME) --build-arg VOLUME_NAME=$(VOLUME_NAME) --build-arg GATEWAY_NAME=$(GATEWAY_NAME) --build-arg DATASET_NAME=$(DATASET_NAME)

.PHONY: all build run push

all: run

base:
	$(MAKE) -C ../containers build

syndicate: base
	$(eval NAME := data-containers-$(DATASET_NAME))
	$(eval DOCKERFILE := ../containers/Dockerfile.syndicate)
	-@mkdir ../containers/cert/
	@cp $(USER_NAME).pkey ../containers/cert/
	@docker inspect -f '{{.Id}}' $(NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build -f $(DOCKERFILE) -t $(NAME) $(DOCKER_ARGS) ../containers ; fi
	-@rm -rf ../containers/cert

build: syndicate

run: syndicate
	@docker run -ti --cap-add SYS_ADMIN --device /dev/fuse --privileged data-containers-$(DATASET_NAME)

push: build
	docker tag data-containers-$(DATASET_NAME) syndicatestorage/pov-anaconda
	docker push syndicatestorage/pov-anaconda
