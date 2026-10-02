"""Deliberately simplified atmospheric-entry utilities.

This module is for intuition and relative comparisons, not vehicle sizing,
human-rating, guidance, or flight operations.
"""

from math import exp, sqrt

from .constants import ATMOSPHERE_SCALE_HEIGHT, SEA_LEVEL_DENSITY


def density_exponential(altitude_m: float) -> float:
    """Toy atmospheric density model in kg/m^3."""
    altitude_m = max(0.0, altitude_m)
    return SEA_LEVEL_DENSITY * exp(-altitude_m / ATMOSPHERE_SCALE_HEIGHT)


def dynamic_pressure(*, density: float, speed: float) -> float:
    """Dynamic pressure q = 1/2 rho v^2 in Pa."""
    return 0.5 * density * speed**2


def ballistic_drag_acceleration(
    *,
    density: float,
    speed: float,
    ballistic_coefficient: float,
) -> float:
    """Drag deceleration magnitude in m/s^2.

    ballistic_coefficient = mass / (Cd * area), in kg/m^2.
    """
    if ballistic_coefficient <= 0:
        raise ValueError("ballistic_coefficient must be positive.")
    return dynamic_pressure(density=density, speed=speed) / ballistic_coefficient


def heating_proxy(
    *,
    density: float,
    speed: float,
    nose_radius_m: float = 1.0,
) -> float:
    """Dimensionless-ish convective-heating proxy proportional to sqrt(rho/R)*v^3.

    It intentionally omits the empirical calibration coefficient. The output is
    useful only for relative comparisons inside MoonDrop.
    """
    if nose_radius_m <= 0:
        raise ValueError("nose_radius_m must be positive.")
    return sqrt(max(density, 0.0) / nose_radius_m) * speed**3
