# -*- coding: utf-8 -*-


def test_package_import():
    """Test package imports."""
    import tank_dynamics

    assert tank_dynamics is not None


def test_core_import():
    """Test module imports."""
    from tank_dynamics import core

    assert core is not None

def test_constants_import():
    """Test file imports."""
    from tank_dynamics.core import constants
    
    assert constants is not None
