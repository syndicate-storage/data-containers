DATASET_NAME ?= 
BUILD_FLAG ?=

.PHONY: all build push

all: build

build:
	$(MAKE) -C ./anaconda build DATASET_NAME=$(DATASET_NAME) BUILD_FLAG=$(BUILD_FLAG)

push:
	$(MAKE) -C ./anaconda push DATASET_NAME=$(DATASET_NAME) BUILD_FLAG=$(BUILD_FLAG)
