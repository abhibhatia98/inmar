import logging
from starlette.requests import Request
# from opencensus.trace import config_integration
# from opencensus.trace.attributes_helper import COMMON_ATTRIBUTES
# from opencensus.trace.span import SpanKind

from shared.logging.tracer import initialize_tracer
from shared.reader.config_reader import ConfigReader


# HTTP_URL = COMMON_ATTRIBUTES['HTTP_URL']
# HTTP_STATUS_CODE = COMMON_ATTRIBUTES['HTTP_STATUS_CODE']
log_instrumentation_key = ConfigReader.read_config_parameter("log_instrumentation_key")
tracer = initialize_tracer(connection_str=log_instrumentation_key)
logger = logging.getLogger("shared.logging.logger")  # the class is singleton and gets the logger with azure log handler


# common middle ware to handle request logging
async def azure_request_logging(request: Request, call_next):
    pass
    # config_integration.trace_integrations(['logging'], tracer=tracer)
    # with tracer.span(name='main') as span:
    #     span.span_kind = SpanKind.SERVER
    #     trace_id = request.headers.get("trace_id", None)
    #     if trace_id is None:
    #         request.headers.__dict__['_list'].append(('trace_id'.encode(),
    #                                                   span.context_tracer.span_context.trace_id.encode()))
    #     response = await call_next(request)
    #     try:
    #         tracer.add_attribute_to_current_span(
    #             attribute_key=HTTP_STATUS_CODE,
    #             attribute_value=response.status_code)
    #         tracer.add_attribute_to_current_span(
    #             attribute_key=HTTP_URL,
    #             attribute_value=str(request.url))
    #         tracer.add_attribute_to_current_span(
    #             attribute_key='organization_id',
    #             attribute_value=request.path_params.get('organization_id')
    #         )
    #     except Exception as ex:
    #         logger.error(f"span add failed with error {ex}")
    # return response
