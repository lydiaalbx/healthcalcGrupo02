import pytest
from healthcalc.health_calc_impl import HealthCalcImpl
from healthcalc.exceptions import InvalidHealthDataException


class TestIBW:

    @pytest.fixture(autouse=True)
    def set_up(self):
        # Arrange (común)
        self.health_calc = HealthCalcImpl()

    def test_ibw_valido_hombre(self):
        """Cálculo válido de IBW para hombre."""

        # Arrange
        height = 175.0
        sex = "male"
        expected_ibw = 50 + 0.9 * (height - 152.4)

        # Act
        result = self.health_calc.ibw(height, sex)

        # Assert
        assert result == pytest.approx(expected_ibw, abs=0.01)

    def test_ibw_valido_mujer(self):
        """Cálculo válido de IBW para mujer."""

        # Arrange
        height = 165.0
        sex = "female"
        expected_ibw = 45.5 + 0.9 * (height - 152.4)

        # Act
        result = self.health_calc.ibw(height, sex)

        # Assert
        assert result == pytest.approx(expected_ibw, abs=0.01)

    def test_ibw_altura_cero(self):
        """Altura 0 debe lanzar excepción."""

        # Arrange
        height = 0.0
        sex = "male"

        # Act
        action = lambda: self.health_calc.ibw(height, sex)

        # Assert
        with pytest.raises(InvalidHealthDataException):
            action()

    def test_ibw_altura_negativa(self):
        """Altura negativa debe lanzar excepción."""

        # Arrange
        height = -10.0
        sex = "female"

        # Act
        action = lambda: self.health_calc.ibw(height, sex)

        # Assert
        with pytest.raises(InvalidHealthDataException):
            action()

    def test_ibw_altura_muy_baja(self):
        """Altura < 30 debe lanzar excepción."""

        # Arrange
        height = 20.0
        sex = "male"

        # Act
        action = lambda: self.health_calc.ibw(height, sex)

        # Assert
        with pytest.raises(InvalidHealthDataException):
            action()

    def test_ibw_altura_muy_alta(self):
        """Altura > 300 debe lanzar excepción."""

        # Arrange
        height = 350.0
        sex = "male"

        # Act
        action = lambda: self.health_calc.ibw(height, sex)

        # Assert
        with pytest.raises(InvalidHealthDataException):
            action()

    def test_ibw_sexo_invalido(self):
        """Sexo inválido debe lanzar excepción."""

        # Arrange
        height = 165.0
        sex = "other"

        # Act
        action = lambda: self.health_calc.ibw(height, sex)

        # Assert
        with pytest.raises(InvalidHealthDataException):
            action()
    