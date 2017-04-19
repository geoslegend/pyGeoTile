import pytest
from pygeotile.meta import Meta


def test_meta():
    meta = Meta()

    assert meta.tile_size == 256
    assert meta.earth_radius == 6378137


def test_zoom_exception():
    meta = Meta()
    with pytest.raises(Exception) as exception:
        _ = meta.zoom
    assert 'Zoom is not set!' in str(exception.value)