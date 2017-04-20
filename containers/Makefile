.PHONY: all build

all: build

base:
	$(eval NAME := data-containers-base)
	$(eval DOCKERFILE := ../containers/Dockerfile.base)
	@docker inspect -f '{{.Id}}' $(NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build -f $(DOCKERFILE) -t $(NAME) ../containers ; fi

anaconda: base
	$(eval NAME := data-containers-anaconda)
	$(eval DOCKERFILE := ../containers/Dockerfile.anaconda)
	@docker inspect -f '{{.Id}}' $(NAME) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build -f $(DOCKERFILE) -t $(NAME) ../containers ; fi

build: anaconda
