import geocoder
from typing import NamedTuple, List

from exceptions import CantGetCoordinates
from constants import USE_ROUNDED_COORDS


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:
    """Returns current GPS coordinates"""
    coordinates = _get_my_coordinates()
    return _round_coordinates(coordinates)


def _get_my_coordinates() -> Coordinates:
    try:
        myloc = geocoder.ip('me')
    except CantGetCoordinates:
        raise CantGetCoordinates
    return _parse_coordinates(myloc.latlng)


def _parse_coordinates(get_my_output: List[float]) -> Coordinates:
    if len(get_my_output) != 2:
        raise CantGetCoordinates
    latitude, longitude = [_parse_float_coordinate(val)
                           for val in get_my_output]
    return Coordinates(latitude=latitude, longitude=longitude)


def _parse_float_coordinate(value: float) -> float:
    if type(value) != float:
        raise CantGetCoordinates
    return value


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not USE_ROUNDED_COORDS:
        return coordinates
    latitude, longitude = list(
        map(lambda x: round(x, 2), [coordinates.latitude, coordinates.longitude]))
    return Coordinates(latitude=latitude, longitude=longitude)


if __name__ == "__main__":
    print(get_coordinates())
