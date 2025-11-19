from arrange1 import Packages
pkg=Packages()
def test_standard_small():
    assert pkg.sort(50, 40, 30, 5) == "STANDARD"

def test_bulky_due_to_dimension():
    assert pkg.sort(150, 20, 20, 5) == "SPECIAL"

def test_bulky_due_to_volume():
    assert pkg.sort(100, 100, 100, 1) == "SPECIAL"

def test_heavy():
    assert pkg.sort(10, 10, 10, 20) == "SPECIAL"

def test_rejected_heavy_and_bulky():
    assert pkg.sort(200, 200, 10, 25) == "REJECTED"

def test_not_heavy_just_below_threshold():
    assert pkg.sort(100, 100, 99.9999, 19.999) == "STANDARD"

def test_heavy_edge_case():
    assert pkg.sort(100, 100, 100, 20.0) == "REJECTED"

def test_dimension_edge_case():
    assert pkg.sort(150, 10, 10, 1) == "SPECIAL"

def test_large_volume_rejected_when_heavy():
    assert pkg.sort(200, 200, 200, 21) == "REJECTED"