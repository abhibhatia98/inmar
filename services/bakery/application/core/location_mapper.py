from bakery.application.dto.location_dto import LocationDTO
from bakery.domain.model.location import Location


class LocationMapper:
    """
    map different data to objects
    """

    def map_location_dto(self, location: Location) -> LocationDTO:
        return LocationDTO(location_id=location.id,
                           location_name=location.name,
                           description=location.description,
                           updated_by=location.updated_by)
