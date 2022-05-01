
from bakery.application.dto.dto import DTO


class DepartmentDTO(DTO):
    def __init__(self, department_name: str, department_email: str, department_contact: str):
        self.department_name = department_name
        self.department_email = department_email
        self.department_contact = department_contact
