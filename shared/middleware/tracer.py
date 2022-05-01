import uuid

import opentracing
from opentracing import Format, ext, tags


def before_http_request(request, tracer):
    span_context = tracer.extract(
        format=Format.HTTP_HEADERS,
        carrier=request.headers,
    )
    span = tracer.start_span( operation_name=request.method,
                              child_of=span_context)
    trace_id = str(uuid.uuid4())
    span.set_baggage_item('trace_id', trace_id)
    span.set_tag(tags.HTTP_URL, request.url)

    http_header_carrier= {}
    opentracing.global_tracer().inject(
        span_context=span,
        format=Format.HTTP_HEADERS,
        carrier=http_header_carrier)
    return span
