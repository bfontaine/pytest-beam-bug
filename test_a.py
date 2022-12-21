import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline as TPipeline
from apache_beam.testing.util import equal_to, assert_that

def test_failure():
    with TPipeline() as p:
        assert_that(
            (p | beam.Create([1, 2, 3])),
            equal_to([
                1, 2, 4
            ])
        )
