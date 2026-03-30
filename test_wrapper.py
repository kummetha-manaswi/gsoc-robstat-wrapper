from wrapper import loc_scale_m, scale_m


def test_functions():
    data = [1, 2, 3, 100, 5]

    loc = loc_scale_m(data)
    scale = scale_m(data)

    assert isinstance(loc, list)
    assert len(loc) >= 2
    assert isinstance(scale, float)
