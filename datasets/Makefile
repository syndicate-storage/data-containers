BUILD_FLAG ?=

DATASETS = "pov" "digbio" "imicrobe" "ivirus" "panzea"
APPS = "base" "anvio" "anaconda" "jupyter"

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
