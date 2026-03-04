from abc import ABC, abstractmethod
from healthcalc import InvalidHealthDataException


class HealthCalc(ABC):
    """Interface for the calculator of health parameters."""

    @abstractmethod
    def bmi(self, weight: float, height: float) -> float:
        """Calculate Body Mass Index.

        :param weight: Weight (kg)
        :param height: Height (m)
        :return: BMI value
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def bmi_classification(self, bmi: float) -> str:
        """Calculate the BMI classification of a person.

        :param bmi: Body Mass Index (kg/m2)
        :return: String classification
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def bmi_full_classification(self, bmi: float) -> str:
        """Calculate the FULL BMI classification of a person.

        :param bmi: Body Mass Index (kg/m2)
        :return: String classification (FULL)
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def ibw(self, height: float, sex: str) -> float:
        """Calculate Ideal Body Weight (IBW).

        :param height: Height (cm)
        :param sex: male or female
        :return: IBW value
        :raises InvalidHealthDataException: If data is out of range
        """
        pass

    @abstractmethod
    def bmr(self, weight: float, height: float, age: int, sex: str) -> float:
        """Calculate Basal Metabolic Rate (BMR).

        :param weight: Weight (kg)
        :param height: Height (cm)
        :param age: Age (years)
        :param sex: male or female
        :return: BMR value
        :raises InvalidHealthDataException: If data is out of range
        """
        pass
    
    
    
    

    
    
    
    
    
    