"""Reference constants used by the baseline models.

Values are intentionally centralized so every simulation uses the same units.
SI units throughout.
"""

G = 6.67430e-11

M_EARTH = 5.97219e24
R_EARTH = 6_371_000.0
MU_EARTH = G * M_EARTH

M_MOON = 7.342e22
R_MOON = 1_737_400.0
MU_MOON = G * M_MOON

MEAN_EARTH_MOON_DISTANCE = 384_400_000.0

# Nominal atmospheric-interface altitude used only for baseline calculations.
ENTRY_INTERFACE_ALTITUDE = 100_000.0

# Toy exponential atmosphere parameters. Useful for intuition, not design.
SEA_LEVEL_DENSITY = 1.225
ATMOSPHERE_SCALE_HEIGHT = 8_500.0
