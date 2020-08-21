__version__ = "$Version: 1.4.0"

from typing import Union


class STS_Value(object):
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

    set_values(p_value: float, assignment: str, category: Union[int, str])
        It set all the attributes together: p_value, assignment and category.
    """
    __p_value: Union[float, None]
    __assignment: Union[bool, None]
    __category = Union[int, None]
    __minimum_to_pass: float = 0.01
    __test_name: str

    def __init__(self, test_name: str):
        self.__test_name = test_name
        self.reset()

    def __str__(self):
        if self.__p_value == None:
            return 'There is not record'

        else:
            return f'[{self.p_value}, "{self.assignment}", {self.category}],'

    def reset(self):
        """reset() -> None
        Reset all values from the object
        """
        self.__p_value = None
        self.__assignment = None
        self.__category = None

    @property
    def p_value(self):
        return self.__p_value

    @p_value.setter
    def p_value(self, p_value: float):
        self.__p_value = p_value

        self.__assignment = True if self.__p_value >= self.__minimum_to_pass else False

    @property
    def assignment(self):
        return 'SUCCESS' if self.__assignment else 'FAILURE'

    @assignment.setter
    def assignment(self, assignment: str):
        bool_assignment: bool

        if self.__p_value == None:
            raise ValueError("p_value must be set first")

        if assignment != None:
            assignment = assignment.upper()

            if assignment in ['SUCCESS', 'FAILURE']:
                bool_assignment = True if assignment == 'SUCCESS' else False

                # BEGIN Criteria check
                if bool_assignment != self.__assignment:
                    print(self.__test_name, self.__assignment)
                    raise ValueError("The value does not correspond to the " +
                                     f"criterion, {self.__p_value} should be " +
                                     ("SUCCESS" if verify_assignment else "FAILURE"))
                # END Criteria check

            else:
                raise ValueError("The value must be SUCCESS or FAILURE")

    @property
    def category(self):
        # TODO Investigate what the criteria is for assigning category
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

    def set_values(self, p_value: float, assignment: str, category: Union[int, str]):
        """set_values(self, p_value: float, assignment: str, category: Union[int, str]) -> None

        It set all the attributes together: p_value, assignment and category.

        PARAMETERS
        ----------
        p_value : float
            P-Value to evaluation

        assignment : str
            SUCCESS or FAILURE.  None If not exist values yet

        category : int
            Value for category between 1 and 10

        """
        self.p_value = p_value
        self.assignment = assignment
        self.category = category
