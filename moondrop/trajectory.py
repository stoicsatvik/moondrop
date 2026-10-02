"""First-order trajectory energetics.

These functions deliberately stay simple and auditable. They are useful for
order-of-magnitude reasoning before a full numerical Earth-Moon propagator is
introduced.
"""

from math import sqrt

from .constants import (
    ENTRY_INTERFACE_ALTITUDE,
    MEAN_EARTH_MOON_DISTANCE,
    MU_EARTH,
    MU_MOON,
    R_EARTH,
    R_MOON,
)


def escape_velocity(mu: float, radius: float) -> float:
    """Return two-body escape speed in m/s."""
    return sqrt(2.0 * mu / radius)


def lunar_surface_escape_velocity() -> float:
    """Idealized escape speed from the lunar surface."""
    return escape_velocity(MU_MOON, R_MOON)


def speed_from_energy_fall(
    *,
    mu: float,
    start_radius: float,
    end_radius: float,
    start_speed: float = 0.0,
) -> float:
    """Speed after a radial two-body fall using conservation of specific energy.

    This ignores angular momentum, third bodies, atmosphere and guidance.
    """
    if start_radius <= 0 or end_radius <= 0:
        raise ValueError("Radii must be positive.")
    if end_radius >= start_radius:
        raise ValueError("end_radius must be smaller than start_radius.")
    v2 = start_speed**2 + 2.0 * mu * (1.0 / end_radius - 1.0 / start_radius)
    return sqrt(max(v2, 0.0))


def earth_interface_speed_from_lunar_distance(start_speed: float = 0.0) -> float:
    """Toy geocentric fall speed from lunar distance to 100 km altitude.

    This is NOT a real lunar-return trajectory. It exists to show the energy
    scale before patched-conic / n-body propagation is implemented.
    """
    return speed_from_energy_fall(
        mu=MU_EARTH,
        start_radius=MEAN_EARTH_MOON_DISTANCE,
        end_radius=R_EARTH + ENTRY_INTERFACE_ALTITUDE,
        start_speed=start_speed,
    )


def specific_kinetic_energy(speed: float) -> float:
    """Specific kinetic energy in J/kg."""
    return 0.5 * speed**2
