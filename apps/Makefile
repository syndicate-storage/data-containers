BUILD_FLAG ?=

APPS = "anvio" "anaconda" "jupyter"

.PHONY: all build push

all: build

build:
	$(foreach var, $(APPS), $(MAKE) -C ./$(var) build BUILD_FLAG=$(BUILD_FLAG);)

push:
	$(foreach var, $(APPS), $(MAKE) -C ./$(var) push BUILD_FLAG=$(BUILD_FLAG);)
