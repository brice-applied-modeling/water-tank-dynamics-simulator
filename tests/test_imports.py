# -*- coding: utf-8 -*-

def test_constants_import():
    """Test to ensure src layout module is callable."""
    from tank_dynamics.core import constants
    
    assert constants is not None
