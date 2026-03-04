import pytest
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException


class TestMifflinStJeor:

    @pytest.fixture(autouse=True)
    def set_up(self):
        """Executed before each test."""
        self.health_calc = HealthCalcImpl()

    # --- Valid calculations ---

    def test_bmr_valido_hombre(self):
        """Valid BMR calculation for male."""

        # Arrange
        weight = 70
        height = 175
        age = 25
        sex = "male"
        expected = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)

        # Act
        result = self.health_calc.bmr(weight, height, age, sex)

        # Assert
        assert result == pytest.approx(expected, abs=0.01)

    def test_bmr_valido_mujer(self):
        """Valid BMR calculation for female."""

        # Arrange
        weight = 60
        height = 165
        age = 30
        sex = "female"
        expected = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

        # Act
        result = self.health_calc.bmr(weight, height, age, sex)

        # Assert
        assert result == pytest.approx(expected, abs=0.01)

    # --- Validation tests ---

    def test_bmr_peso_cero(self):
        """Weight = 0 should raise exception."""

        # Arrange
        weight = 0
        height = 175
        age = 25
        sex = "male"

        # Act + Assert
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmr(weight, height, age, sex)

    def test_bmr_altura_cero(self):
        """Height = 0 should raise exception."""

        # Arrange
        weight = 70
        height = 0
        age = 25
        sex = "male"

        # Act + Assert
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmr(weight, height, age, sex)

    def test_bmr_edad_cero(self):
        """Age = 0 should raise exception."""

        # Arrange
        weight = 70
        height = 175
        age = 0
        sex = "male"

        # Act + Assert
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmr(weight, height, age, sex)

    def test_bmr_edad_fuera_rango(self):
        """Age above biological range should raise exception."""

        # Arrange
        weight = 70
        height = 175
        age = 130
        sex = "male"

        # Act + Assert
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmr(weight, height, age, sex)

    def test_bmr_sexo_invalido(self):
        """Invalid sex should raise exception."""

        # Arrange
        weight = 70
        height = 175
        age = 25
        sex = "other"

        # Act + Assert
        with pytest.raises(InvalidHealthDataException):
            self.health_calc.bmr(weight, height, age, sex)