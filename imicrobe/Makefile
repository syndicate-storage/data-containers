MS_URL ?= demo1.opencloud.cs.arizona.edu:28080
USER_NAME ?= suser1@syndicate.org
VOLUME_NAME ?= pov
GATEWAY_NAME ?= ug_pov_anonymous
DATASET_NAME ?= imicrobe

DOCKER_ARGS = --build-arg MS_URL=$(MS_URL) --build-arg USER_NAME=$(USER_NAME) --build-arg VOLUME_NAME=$(VOLUME_NAME) --build-arg GATEWAY_NAME=$(GATEWAY_NAME) --build-arg DATASET_NAME=$(DATASET_NAME)

.PHONY: all build run

all: run

base:
	$(eval NAME := data-containers-base)
	$(eval DOCKERFILE := ../containers/Dockerfile.base)
	@docker inspect -f '{{.Id}}' $(NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build -f $(DOCKERFILE) -t $(NAME) ../containers ; fi

anaconda: base
	$(eval NAME := data-containers-anaconda)
	$(eval DOCKERFILE := ../containers/Dockerfile.anaconda)
	@docker inspect -f '{{.Id}}' $(NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build -f $(DOCKERFILE) -t $(NAME) ../containers ; fi

syndicate: anaconda
	$(eval NAME := data-containers-$(DATASET_NAME))
	$(eval DOCKERFILE := ../containers/Dockerfile.syndicate)
	-@mkdir ../containers/cert/
	@cp $(USER_NAME) ../containers/cert/
	@docker inspect -f '{{.Id}}' $(NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build -f $(DOCKERFILE) -t $(NAME) $(DOCKER_ARGS) ../containers ; fi
	-@rm -rf ../containers/cert

build: syndicate
	

run: syndicate
	@docker run -ti --cap-add SYS_ADMIN --device /dev/fuse --privileged data-containers-$(DATASET_NAME)
