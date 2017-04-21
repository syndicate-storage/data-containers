BUILD_FLAG ?=

.PHONY: all build

all: build

syndicate:
	$(eval NAME := data-containers-syndicate)
	$(eval DOCKERFILE := ../containers/Dockerfile.syndicate)
	@docker inspect -f '{{.Id}}' $(NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build $(BUILD_FLAG) -f $(DOCKERFILE) -t $(NAME) ../containers ; fi

anaconda: syndicate
	$(eval NAME := data-containers-anaconda)
	$(eval DOCKERFILE := ../containers/Dockerfile.anaconda)
	@docker inspect -f '{{.Id}}' $(NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build $(BUILD_FLAG) -f $(DOCKERFILE) -t $(NAME) ../containers ; fi

build: anaconda
