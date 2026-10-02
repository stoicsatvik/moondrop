# MoonDrop

**MoonDrop asks one question:** how close can a human mission get to a literal Moon-to-Earth freefall without violating physics or survivability?

This repository is a research and simulation sandbox for the problem. It is **not flight software** and does not contain operational human-jump instructions.

## First-principles model

A Moon-to-Earth "jump" decomposes into four regimes:

1. **Lunar departure** — escape the Moon's gravity well.
2. **Cislunar transfer** — fall through the Earth-Moon gravitational system.
3. **Atmospheric interface** — arrive near Earth at roughly interplanetary re-entry-class velocity.
4. **Energy disposal** — convert enormous kinetic energy into heat, drag, lift, radiation and ultimately a survivable landing.

The core optimization problem is:

```
maximize   free_flight_fraction
minimize   protective_system_mass
subject to thermal, pressure, acceleration and trajectory constraints
```

The interesting boundary is not "can a person jump from the Moon?" A naked human cannot survive Earth entry. The interesting boundary is:

> **What is the minimum protective system that can bridge the gap between a human body and the physics of lunar-return re-entry?**

## What exists now

- `moondrop/constants.py` — physical constants and reference values
- `moondrop/trajectory.py` — escape velocity and two-body energy calculations
- `moondrop/entry.py` — deliberately simple atmosphere, drag and heating-proxy model
- `scripts/run_baseline.py` — prints the first MoonDrop baseline
- `tests/` — sanity checks against known order-of-magnitude physics
- `docs/MISSION.md` — research program and validation ladder

## Run

```bash
python -m scripts.run_baseline
pytest
```

## Model philosophy

Every model must expose:

- assumptions
- units
- equations
- uncertainty
- validation target
- failure cases

A beautiful plot with hidden assumptions is just numerically decorated fan fiction.

## Immediate milestones

- [x] Establish first-principles constants and baseline energetics
- [x] Quantify lunar escape and Earth-arrival velocity
- [x] Add a toy atmospheric-entry model
- [ ] Replace patched-conic estimate with a numerical Earth-Moon propagator
- [ ] Add trajectory plots and energy bookkeeping
- [ ] Benchmark against Apollo lunar-return data
- [ ] Add uncertainty / Monte Carlo analysis
- [ ] Separate "exposed human", "wearable system", and "vehicle" architectures
- [ ] Build a survivability constraint model from published aerospace medicine data
- [ ] Add thermal protection trade-space models only after validation

## Safety / scope

MoonDrop is currently an educational numerical research project. Human-rated aerospace systems require professional engineering, testing, medical review, regulatory approval and independent safety analysis. Nothing here should be treated as a procedure for an actual jump or re-entry.
