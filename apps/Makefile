BUILD_FLAG ?= --squash

APPS = "base" "anvio" "anaconda" "jupyter" "mash"

.PHONY: all clean build rebuild push repush

all: build

clean:
	$(foreach var, $(APPS), $(MAKE) -C ./$(var) clean;)

build:
	$(foreach var, $(APPS), $(MAKE) -C ./$(var) build BUILD_FLAG=$(BUILD_FLAG);)

rebuild:
	$(foreach var, $(APPS), $(MAKE) -C ./$(var) rebuild BUILD_FLAG=$(BUILD_FLAG);)

push:
	$(foreach var, $(APPS), $(MAKE) -C ./$(var) push BUILD_FLAG=$(BUILD_FLAG);)

repush:
	$(foreach var, $(APPS), $(MAKE) -C ./$(var) repush BUILD_FLAG=$(BUILD_FLAG);)
