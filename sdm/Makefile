BUILD_FLAG ?= --squash

APPS = "base" "anvio" "anaconda" "jupyter" "mash"

.PHONY: all clean build rebuild push repush test

all: build

clean:
	docker rmi syndicatestorage/sdm
	$(foreach a, $(APPS), \
		CONTAINERS="$(shell docker ps -a -q --filter=ancestor=sdm-$(a) | awk '{print $$1}')" ; if [ ! -z "$$CONTAINERS" ] ; then docker rm $$CONTAINERS ; fi ; \
		docker inspect -f '{{.Id}}' syndicatestorage/sdm-$(a) 2> /dev/null ; if [ $$? -eq 0 ] ; then docker rmi -f syndicatestorage/sdm-$(a) ; fi ; \
		docker inspect -f '{{.Id}}' sdm-$(a) 2> /dev/null ; if [ $$? -eq 0 ] ; then docker rmi -f sdm-$(a) ; fi ; \
		DANGLINGS="$(shell docker images -f "dangling=true" -q)" ; if [ ! -z "$$DANGLINGS" ] ; then docker rmi $$DANGLINGS ; fi ; \
	)

build:
	$(foreach a, $(APPS), \
		sed "s/%%IMAGE_BASE%%/syndicate-$(a)/" ./Dockerfile.template > ./Dockerfile ; \
		docker inspect -f '{{.Id}}' sdm-$(a) 2> /dev/null ; if [ $$? -ne 0 ] ; then docker build $(BUILD_FLAG) -f ./Dockerfile -t sdm-$(a) . ; fi ; \
		docker tag sdm-$(a) syndicatestorage/sdm-$(a) ; \
		rm -f ./Dockerfile ; \
	)
	docker tag sdm-base syndicatestorage/sdm

rebuild: clean build

push: build
	$(foreach a, $(APPS), \
		docker push syndicatestorage/sdm-$(a) \
	;)
	docker push syndicatestorage/sdm

repush: clean push
