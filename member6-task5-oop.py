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
class Metal(Material):
    def __init__(self, name: str, properties: MaterialProperties, is_ferrous: bool = False):
        super().__init__(name, properties)
        self.is_ferrous = is_ferrous
class StressStrainTest:
    def __init__(self, material: Material, force: float, area: float, original_length: float, change_in_length: float):
        self.material = material
        self._force = force
        self._area = area
        self._original_length = original_length
        self._change_in_length = change_in_length    

        if force <= 0 or area <= 0 or original_length <= 0:
            raise ValueError("Force, area, and original length must be positive.")

    @property
    def stress(self) -> float:
        """Calculate stress in Pascals (Pa). Formula: F / A"""
        return self._force / self._area

    @property
    def stress_mpa(self) -> float:
        """Convert Pa to MPa for material failure checks."""
        return self.stress / 1_000_000

    @property
    def strain(self) -> float:
        """Calculate strain (dimensionless). Formula: dL / L0"""
        return self._change_in_length / self._original_length

    @property
    def youngs_modulus(self) -> float:
        """Calculate Young's modulus in GPa."""
        return (self.stress_mpa / self.strain) / 1000
    
    def will_fail(self) -> bool:
        return not self.material.can_withstand_stress(self.stress_mpa)

    # Example Usage

#create properties
steel_props = MaterialProperties(density=7850, yield_strength=250, typical_youngs_modulus=200)
aluminum_props = MaterialProperties(density=2700, yield_strength=276, typical_youngs_modulus=69)
titanium_props = MaterialProperties(density=4500, yield_strength=830, typical_youngs_modulus=116)

#create materials
steel = Metal("Steel", steel_props, is_ferrous=True)
aluminum = Metal("Aluminum", aluminum_props, is_ferrous=False)
titanium = Metal("Titanium", titanium_props, is_ferrous=False)