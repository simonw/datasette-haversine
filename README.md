# datasette-haversine

[![PyPI](https://img.shields.io/pypi/v/datasette-haversine.svg)](https://pypi.org/project/datasette-haversine/)
[![CircleCI](https://circleci.com/gh/simonw/datasette-haversine.svg?style=svg)](https://circleci.com/gh/simonw/datasette-haversine)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-haversine/blob/master/LICENSE)

Datasette plugin that adds a custom SQL function for haversine distances

Install this plugin in the same environment as Datasette to enable the `haversine()` SQL function.

    $ pip install datasette-haversine

The plugin is built on top of the [haversine](https://github.com/mapado/haversine) library.

## haversine() to calculate distances

```sql
select haversine(lat1, lon1, lat2, lon2);
```

This will return the distance in kilometers between the point defined by `(lat1, lon1)` and the point defined by `(lat2, lon2)`.

## Custom units

By default `haversine()` returns results in km. You can pass an optional third argument to get results in a different unit:

- `ft` for feet
- `m` for meters
- `in` for inches
- `mi` for miles
- `nmi` for nautical miles
- `km` for kilometers (the default)

```sql
select haversine(lat1, lon1, lat2, lon2, 'mi');
```
