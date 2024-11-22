import pytest

from service.avis_service import ServiceAvis


def test_validation_avis_invalide_ok():
    """message invalide ok"""
    avis = "tu es une merde"
    invalide = ServiceAvis().Validation_avis(message_avis=avis)
    assert invalide is False


def test_validation_avis_valide_ok():
    """message valide ok"""
    avis = "convenable"
    invalide = ServiceAvis().Validation_avis(message_avis=avis)
    assert invalide is True


if __name__ == "__main__":

    pytest.main([__file__])
