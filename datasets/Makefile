BUILD_FLAG ?= --squash

DATASETS = "pov" "imicrobe" "ivirus" "eht2013"
#"digbio" "panzea"
APPS = "base" "anvio" "anaconda" "jupyter" "mash"

.PHONY: all clean build rebuild push repush

all: build

clean:
	$(foreach d, $(DATASETS), \
		$(foreach a, $(APPS), \
			$(MAKE) -C ./$(d) clean \
		;)\
	)

build:
	$(foreach d, $(DATASETS), \
		$(foreach a, $(APPS), \
			$(MAKE) -C ./$(d) build APP_NAME=$(a) BUILD_FLAG=$(BUILD_FLAG) \
		;)\
	)

rebuild:
	$(foreach d, $(DATASETS), \
		$(foreach a, $(APPS), \
			$(MAKE) -C ./$(d) rebuild APP_NAME=$(a) BUILD_FLAG=$(BUILD_FLAG) \
		;)\
	)

push:
	$(foreach d, $(DATASETS), \
		$(foreach a, $(APPS), \
			$(MAKE) -C ./$(d) push APP_NAME=$(a) BUILD_FLAG=$(BUILD_FLAG) \
		;)\
	)

repush:
	$(foreach d, $(DATASETS), \
		$(foreach a, $(APPS), \
			$(MAKE) -C ./$(d) repush APP_NAME=$(a) BUILD_FLAG=$(BUILD_FLAG) \
		;)\
	)
