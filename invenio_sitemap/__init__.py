# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-FileCopyrightText: 2025 Northwestern University.
# SPDX-FileCopyrightText: 2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Sitemap indices and sitemaps for InvenioRDM."""

from .cache import SitemapCache, SitemapIndexCache
from .ext import InvenioSitemap
from .sitemap import SitemapSection
from .utils import format_to_w3c, iterate_urls_of_sitemap_indices

__version__ = "1.0.0"

__all__ = (
    "__version__",
    "InvenioSitemap",
    "SitemapCache",
    "SitemapIndexCache",
    "SitemapSection",
    "format_to_w3c",
    "iterate_urls_of_sitemap_indices",
)
