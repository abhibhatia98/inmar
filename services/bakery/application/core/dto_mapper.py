from bakery.application.dto.department_dto import DepartmentDTO
from bakery.application.dto.location_dto import LocationDTO
from bakery.domain.model.department import Department
from bakery.domain.model.location import Location


class DTOMapper:
    """
    map different data to objects
    """

    def map_location_dto(self, location: Location) -> LocationDTO:
        return LocationDTO(location_id=location.id,
                           location_name=location.name,
                           description=location.description,
                           updated_by=location.updated_by)

    def map_department_dto(self, department: Department) -> DepartmentDTO:
        return DepartmentDTO(department_id=department.id, location_id=department.location_id,
                             department_name=department.name,
                             department_description=department.description,
                             updated_by=department.updated_by)
