from dataclasses import dataclass
from typing import List

@dataclass
class MaterialProperties:
    density: float  # kg/m
    yield_strength: float  # MPa
    typical_youngs_modulus: float # GPa

    def __post_init__(self):
        if self.density <= 0 or self.yield_strength <= 0 or self.typical_youngs_modulus <= 0:
            raise ValueError("All material properties must be positive values.")
class Material:
    def __init__(self, name: str, properties: MaterialProperties):
        self.name = name
        self.properties = properties
    def can_withstand_stress(self, stress_mpa: float) -> bool:
        """Check if the material can withstand the given stress (in MPa)."""
        return stress_mpa < self.properties.yield_strength