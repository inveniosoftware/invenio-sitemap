# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-FileCopyrightText: 2025 Northwestern University.
# SPDX-License-Identifier: MIT


"""Utils."""

import arrow
from invenio_base import invenio_url_for
from invenio_cache import current_cache

from .cache import SitemapIndexCache


def format_to_w3c(dt):
    """Convert a datetime to a W3C Date and Time format.

    Converts the date to a minute-resolution datetime timestamp with a special
    UTC designator 'Z'. See more information at
    https://www.w3.org/TR/NOTE-datetime.
    """
    dt_arrow_utc = arrow.get(dt).to("utc")
    return dt_arrow_utc.format("YYYY-MM-DDTHH:mm:ss") + "Z"


def parse_from_w3c(dt_w3c_str):
    """Convert a W3C Date and Time formatted string into a datetime."""
    return arrow.get(dt_w3c_str, "YYYY-MM-DDTHH:mm:ssZ").datetime


def iterate_urls_of_sitemap_indices():
    """Return iterable of sitemap indices' URLs."""
    cache = SitemapIndexCache(current_cache)
    for page in cache.iterate_keys():
        yield invenio_url_for("invenio_sitemap.sitemap_index", page=page)
