from datasette import hookimpl
from haversine import haversine


def haversine_sql(lat1, lon1, lat2, lon2, unit="km"):
    return haversine((lat1, lon1), (lat2, lon2), unit=unit)


@hookimpl
def prepare_connection(conn):
    conn.create_function("haversine", 4, haversine_sql)
    conn.create_function("haversine", 5, haversine_sql)
