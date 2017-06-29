BUILD_FLAG ?=

DATASETS = "pov" "imicrobe" "ivirus" "eht2013"
#"digbio" "panzea"
APPS = "base" "anvio" "anaconda" "jupyter" "mash"

.PHONY: all build push

all: build

build:
	$(foreach d, $(DATASETS), \
		$(foreach a, $(APPS), \
			$(MAKE) -C ./$(d) build APP_NAME=$(a) BUILD_FLAG=$(BUILD_FLAG) \
		;)\
	)

push:
	$(foreach d, $(DATASETS), \
		$(foreach a, $(APPS), \
			$(MAKE) -C ./$(d) push APP_NAME=$(a) BUILD_FLAG=$(BUILD_FLAG) \
		;)\
	)
