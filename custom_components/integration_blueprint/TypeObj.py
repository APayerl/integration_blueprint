from dataclasses import dataclass
from typing import Any


@dataclass
class BinType:
    """BinType data class"""

    code: str
    size: float
    unit: str
    container_type: str

    @staticmethod
    def from_dict(obj: Any) -> "BinType":
        """Convert to BinType"""
        return BinType(
            str(obj.get("Code")),
            float(obj.get("Size")),
            str(obj.get("Unit")),
            str(obj.get("ContainerType")),
        )


@dataclass
class Fee:
    """Fee data class"""

    description: str
    bin_type: BinType
    waste_pickups_per_year: int
    waste_pickup_frequency: str
    waste_pickup_frequency_code: str
    waste_type: str
    code: str
    product: str
    part_product: str
    designation: str
    calculated_cost: int
    is_cost_calculated: bool
    part_year_starts: str
    part_year_ends: str
    part_year_description: str
    id: int

    @staticmethod
    def from_dict(obj: Any) -> "Fee":
        """Convert to Fee"""
        return Fee(
            str(obj.get("Description")),
            BinType.from_dict(obj.get("BinType")),
            int(obj.get("WastePickupsPerYear")),
            str(obj.get("WastePickupFrequency")),
            str(obj.get("WastePickupFrequencyCode")),
            str(obj.get("WasteType")),
            str(obj.get("Code")),
            str(obj.get("Product")),
            str(obj.get("PartProduct")),
            str(obj.get("Designation")),
            int(obj.get("CalculatedCost")),
            bool(obj.get("IsCostCalculated")),
            str(obj.get("PartYearStarts")),
            str(obj.get("PartYearEnds")),
            str(obj.get("PartYearDescription")),
            int(obj.get("ID")),
        )


@dataclass
class RhService:
    """RhService data class, base object"""

    next_waste_pickup: str
    waste_pickups_per_year: int
    waste_type: str
    waste_pickup_frequency: str
    waste_pickup_frequency_code: str
    bin_type: BinType
    number_of_bins: float
    fee: Fee
    number_of_bins_antl: int
    is_active: bool
    id: int
    description: str
    start_date: str
    stop_date: str
    building_id: str

    @staticmethod
    def from_dict(obj: Any) -> "RhService":
        """Convert to RhService"""
        return RhService(
            str(obj.get("NextWastePickup")),
            int(obj.get("WastePickupsPerYear")),
            str(obj.get("WasteType")),
            str(obj.get("WastePickupFrequency")),
            str(obj.get("WastePickupFrequencyCode")),
            BinType.from_dict(obj.get("BinType")),
            float(obj.get("NumberOfBins")),
            Fee.from_dict(obj.get("Fee")),
            int(obj.get("NumberOfBinsAntl")),
            bool(obj.get("IsActive")),
            int(obj.get("ID")),
            str(obj.get("Description")),
            str(obj.get("StartDate")),
            str(obj.get("StopDate")),
            str(obj.get("BuildingID")),
        )


@dataclass
class SearchAddressResult:
    """TypeDef for SearchAddressResult query"""

    succeeded: bool
    buildings: list[str]

    @staticmethod
    def from_dict(obj: Any) -> "SearchAddressResult":
        """Convert to SearchAddressResult"""
        return SearchAddressResult(
            bool(obj.get("Succeeded")), [str(y) for y in obj.get("Buildings")]
        )
