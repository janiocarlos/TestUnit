from TestUnit.run import imc

def test_imc():
    assert imc(80,1.7) == 27
    assert imc(70,1.7) == 24
    