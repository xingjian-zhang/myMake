PYTHON=/Users/jimmy/miniforge3/bin/python

GIT_SNAPSHOT = git --git-dir=.snapshot --work-tree=.

.PHONY: help install snapshot commit synth clean

help:
	@echo "Available targets:"
	@echo "  install    - Install required Python packages from requirements.txt"
	@echo "  snapshot   - Make a git snapshot of the current state"
	@echo "  commit     - Commit to the main git repository"
	@echo "  clean      - Remove the data and results directories"
	@echo "  synth-%%    - Run synth.py for a specific experiment config"
	@echo "  run-%%      - Run main.py for a specific experiment config"
	@echo "  all-synth  - Run synth.py for all synthetic experiment configs"
	@echo "  all-run    - Run main.py for all experiment configs"


install:
	pip install -r requirements.txt

.git: .snapshot
	git init .

.snapshot:
	git init .
	mv .git .snapshot

snapshot:
	@SNAPSHOT_COUNT=$$(${GIT_SNAPSHOT} rev-list --all --count) ; \
	${GIT_SNAPSHOT} add . ; \
	${GIT_SNAPSHOT} commit -m "snapshot@$$((SNAPSHOT_COUNT+1))" || true

commit:
	git commit

data:
	mkdir -p data

clean:
	rm -rf data results

synth-%: data
	${PYTHON} synth.py experiments/$*.yaml

results:
	mkdir -p results

run-%: snapshot results synth
	${PYTHON} main.py experiments/$*.yaml

all-synth: $(patsubst experiments/%.yaml,synth-%,$(wildcard experiments/synthetic_*.yaml))

all-run: $(patsubst experiments/%.yaml,run-%,$(wildcard experiments/config_*.yaml))