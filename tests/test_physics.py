from moondrop.entry import density_exponential, dynamic_pressure
from moondrop.trajectory import (
    earth_interface_speed_from_lunar_distance,
    lunar_surface_escape_velocity,
)


def test_lunar_escape_velocity_order_of_magnitude():
    v = lunar_surface_escape_velocity()
    assert 2300 < v < 2500


def test_toy_earth_interface_velocity_is_reentry_class():
    v = earth_interface_speed_from_lunar_distance()
    assert 10_000 < v < 12_000


def test_density_falls_with_altitude():
    assert density_exponential(0) > density_exponential(10_000)
    assert density_exponential(10_000) > density_exponential(50_000)


def test_dynamic_pressure():
    assert dynamic_pressure(density=1.0, speed=10.0) == 50.0
