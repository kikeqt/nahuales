__version__ = "$Version: 0.0.1"

from typing import Dict
from typing import List

from .sts_value import STS_Value


class STS_Results_Collection(object):
    """Provides a collection of results for STS testing
    """
    _dictionary_results: Dict[str, List[STS_Value]] = {}
