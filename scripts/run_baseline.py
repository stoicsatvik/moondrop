"""Print the first MoonDrop order-of-magnitude baseline."""

from moondrop.trajectory import (
    earth_interface_speed_from_lunar_distance,
    lunar_surface_escape_velocity,
    specific_kinetic_energy,
)


def km_s(v: float) -> float:
    return v / 1000.0


def mj_kg(e: float) -> float:
    return e / 1_000_000.0


def main() -> None:
    lunar_escape = lunar_surface_escape_velocity()
    interface_speed = earth_interface_speed_from_lunar_distance()
    interface_energy = specific_kinetic_energy(interface_speed)

    print("MOONDROP // BASELINE 0")
    print("=" * 32)
    print(f"Ideal lunar surface escape speed : {km_s(lunar_escape):8.3f} km/s")
    print(f"Toy Earth interface speed        : {km_s(interface_speed):8.3f} km/s")
    print(f"Specific KE at interface         : {mj_kg(interface_energy):8.2f} MJ/kg")
    print()
    print("Interpretation:")
    print("- Lunar departure is already a propulsion problem.")
    print("- Earth arrival is a re-entry-energy problem, not ordinary skydiving.")
    print("- Next model: numerical Earth-Moon propagation + validated atmosphere.")


if __name__ == "__main__":
    main()
