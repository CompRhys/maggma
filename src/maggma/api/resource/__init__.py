# isort: off
from maggma.api.resource.core import HeaderProcessor, HintScheme, Resource

# isort: on

from maggma.api.resource.aggregation import AggregationResource
from maggma.api.resource.post_resource import PostOnlyResource
from maggma.api.resource.read_resource import ReadOnlyResource, attach_query_ops
from maggma.api.resource.s3_url import S3URLResource
from maggma.api.resource.submission import SubmissionResource

__all__ = [
    "AggregationResource",
    "HeaderProcessor",
    "HintScheme",
    "PostOnlyResource",
    "ReadOnlyResource",
    "Resource",
    "S3URLResource",
    "SubmissionResource",
    "attach_query_ops",
]
