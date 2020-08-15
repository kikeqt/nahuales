__version__ = "$Version: 0.0.1"

from typing import Union


class STS_Result(object):
    """Store values of NIST STS

    Attributes
    ----------
    p_value : float
        P-Value to evaluation
        
    assignment : str
        SUCCESS or FAILURE.  None If not exist values yet
    
    category : int
        Value for category between 1 and 10
        
    Methods
    -------
    reset()
        Reset all values from the object
    """
    __na = True
    __p_value = 0.0
    __assignment = False
    __category = 0

    def reset(self):
        """reset() -> None
        Reset all values from the object
        """
        self.__na = True
        self.__p_value = None
        self.__assignment = None
        self.__category = None

    @property
    def p_value(self):
        if self.__na:
            return None

        else:
            return self.__p_value

    @p_value.setter
    def p_value(self, p_value: float):
        self.__na = False
        self.__p_value = p_value

    @property
    def assignment(self):
        if self.__na:
            return None

        else:
            if self.__assignment:
                return 'SUCCESS'

            else:
                return 'FAILURE'

    @assignment.setter
    def assignment(self, assignment: str):
        assignment = assignment.upper()

        if assignment == 'SUCCESS':
            self.__assignment = True

        elif assignment == 'FAILURE':
            self.__assignment = False

        else:
            raise ValueError("The value must be SUCCESS or FAILURE")

    @property
    def category(self):
        if self.__na:
            return None

        else:
            return self.__category

    @category.setter
    def category(self, category: Union[int, str]):
        if type(category) == type(''):
            category = category.upper()
            category = int(category[1:])

        if type(category) == type(0):
            if 1 <= category <= 10:
                self.__category = category

            else:
                raise ValueError("The value must be in range 1 to 10")

        else:
            raise ValueError(
                "The value must be integer or string, by example with 'C10'")
