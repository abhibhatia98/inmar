from bakery.application.dto.dto import DTO


class DepartmentDTO(DTO):
    def __init__(self, location_id: str, department_id: str, department_name: str, department_description: str,
                 updated_by: str):
        self.location_id = location_id
        self.department_id = department_id
        self.department_name = department_name
        self.department_description = department_description
        self.updated_by = updated_by
