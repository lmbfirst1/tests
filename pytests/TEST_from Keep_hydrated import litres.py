from Keep_hydrated import litres


@pytest.mark.parametrize("time, expected_exception", [(2, 1),
                                                      (1.4, 0),
                                                      (12.3, 6),
                                                      (0.82, 0),
                                                      (11.8, 5),
                                                      (1787, 893),
                                                      (0, 0)])
def test_litres(time, expected_exception):
    assert litres(time) == expected_exception
