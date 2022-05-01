from pydantic import BaseModel
from shared.logging.custom_dimension import CustomDimension


class LoggingProperties(BaseModel):
    custom_dimensions: CustomDimension

# the properties passed as extra should be of this format and the keys will be available as customDimensions
# in azure monitor
# properties = {'custom_dimensions': {'key_1': 'value_1', 'key_2': 'value_2'}}
