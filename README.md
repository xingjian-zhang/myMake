# Makefile for Reproducible Research
[Design Doc](https://docs.google.com/document/d/1UPJz7uZCYYQ9XBdUQnTe512LCzVPqD-zfsXojo0yFy4/edit#heading=h.njsc1qo13nkm)

## Help

Run
```bash
make init
make install
```
to initialize the project and install the required Python packages.


```bash
Available targets:
  install    - Install required Python packages from requirements.txt
  snapshot   - Make a git snapshot of the current state
  commit     - Commit to the main git repository
  clean      - Remove the data and results directories
  synth-%%    - Run synth.py for a specific experiment config
  run-%%      - Run main.py for a specific experiment config
  all-synth  - Run synth.py for all synthetic experiment configs
  all-run    - Run main.py for all experiment configs
```

## Caveats
- How to keep the snapshots synced with the remote repo?
- Snapshot number is not saved into the results directory. This makes it hard to
  retrieve the code.
- No random seed is enforced.
- No tests are implemented.

## Actionable Items
[P0]
- [ ] Add a description of the project to README.md
- [ ] Implement `test` target. Require all tests to pass before committing and snapshotting.
- [ ] Enforce random seed to ensure reproducibility.
- [ ] Save snapshot number into the results directory along with the results.

[P1]
- [ ] Add a 'sync' target to sync the results directory to a remote location.
- [ ] Come up with other useful targets.