import os
import pytest

@pytest.fixture
def assets_dir():
    # Assuming your assets directory path relative to the test file
    assets_dir = os.path.join(os.path.dirname(__file__), '..', 'assets')
    return assets_dir
