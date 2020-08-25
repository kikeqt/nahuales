__version__ = "$Version: 0.0.2"

from typing import Dict
from typing import List

from .sts_value import STSValue


class STS_Results_Collection(object):
    """Provides a collection of results for STS testing
    """
    _dictionary_results: Dict[str, List[STSValue]] = {}
