# MoonDrop research program

## Thesis

A literal unprotected Moon-to-Earth human jump is incompatible with survivable
Earth atmospheric entry. MoonDrop therefore studies the **boundary between
free-flying human and spacecraft**.

The goal is not to assume an answer. The goal is to continuously shrink the
protective system while preserving physically defensible constraints.

## Architecture classes

### A. Exposed human

Useful as a null hypothesis. It establishes exactly which constraints fail and
by how much.

### B. Wearable protective system

A conceptual regime between pressure suit and tiny re-entry vehicle. MoonDrop
will treat this as a research category, not assume that it is feasible.

### C. Minimal personal entry vehicle

A compact system providing the thermal, structural, attitude and life-support
functions that cannot be reduced to clothing.

### D. Conventional capsule

Reference architecture. Existing lunar-return systems provide validation data
and an upper bound on system complexity.

## Validation ladder

### 0 — analytic sanity checks

Escape velocity, orbital energy, atmospheric-interface velocity and kinetic
energy per unit mass.

### 1 — numerical trajectory

Integrate position and velocity through Earth-Moon gravity. Compare simplified
models against known trajectories.

### 2 — atmosphere

Replace the exponential toy atmosphere with a standard atmospheric model.
Track Mach number, dynamic pressure and deceleration.

### 3 — thermal environment

Introduce validated engineering correlations and compare them with published
lunar-return data. Keep uncertainty explicit.

### 4 — human constraints

Represent acceleration, pressure, oxygen, temperature and duration limits as
constraints sourced from aerospace-medicine literature.

### 5 — architecture optimization

Search over conceptual architectures while minimizing mass and maximizing the
fraction of the mission that qualifies as genuine unpowered free flight.

## Required outputs for every simulation

Each run should eventually produce:

- initial state
- assumptions and model version
- trajectory vs time
- velocity vs altitude
- specific mechanical energy vs time
- dynamic pressure vs time
- acceleration vs time
- thermal proxy / validated heat-rate estimate
- constraint violations
- uncertainty bounds

## Scientific discipline

MoonDrop uses a hierarchy:

**analytic equation → numerical model → independent reference → sensitivity
analysis → only then architecture claims.**

If a result cannot survive that chain, it is not a MoonDrop result yet.

## Near-term issue queue

1. Implement RK4 state propagation.
2. Add Earth and Moon point-mass gravity.
3. Validate against a circular lunar orbit before attempting transfer cases.
4. Add event detection for Earth atmospheric interface.
5. Create plots and CSV run artifacts.
6. Benchmark the interface conditions against published Apollo return data.
7. Add unit-aware calculations.
8. Add Monte Carlo perturbations.
9. Build a constraint engine.
10. Write an architecture-comparison notebook.

## Operational boundary

No code in this repository should be interpreted as human-rated flight
software or as instructions for performing an actual jump. Real human
spaceflight requires professional aerospace engineering, testing, medical
oversight, regulation and independent safety review.
