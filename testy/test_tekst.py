def test_always_passes():
    assert 17 == 17

def test_always_fails():
    assert 17 == 18

def test_uppercase():
    assert "loud noises".replace(" ", "-") == "loud-noises"

import pytest

@pytest.fixture
def example_fixture_tekst():
    return "Dzis jest pieknie"

def test_with_fixture(example_fixture_tekst):
    assert len(example_fixture_tekst)  == 17
