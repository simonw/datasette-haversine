from datasette_haversine import prepare_connection
import sqlite3
import pytest

LONDON = 51.513, -0.131
PARIS = 48.87, 2.311


@pytest.fixture
def conn():
    conn = sqlite3.connect(":memory:")
    prepare_connection(conn)
    return conn


@pytest.mark.parametrize(
    "unit,expected",
    (
        ("ft", 1120114.909),
        ("m", 341411.024),
        ("in", 13441378.915),
        ("mi", 212.143),
        ("nmi", 184.3472),
        ("km", 341.411),
    ),
)
def test_haversine(conn, unit, expected):
    actual = conn.execute(
        "select haversine(?, ?, ?, ?, ?)",
        [LONDON[0], LONDON[1], PARIS[0], PARIS[1], unit],
    ).fetchall()[0][0]
    assert expected == pytest.approx(actual)
