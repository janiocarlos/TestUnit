from run import imc,metaPeso

def test_imc():
    assert imc(80,1.7) == 27
    assert imc(70,1.7) == 24

def test_metaPeso():
    assert metaPeso(100,80) == 20
    assert metaPeso(120,90) == 30