"""This is a test script to test flask application"""
from ..wsgi import app

def test_bp_usage():
    """Test if there is blueprint registered"""
    assert app.blueprints.keys(), "No Blueprint Registered!"
