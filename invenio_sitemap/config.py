# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-FileCopyrightText: 2025 Northwestern University.
# SPDX-License-Identifier: MIT

"""Configuration."""

SITEMAP_MAX_ENTRY_COUNT = 10000
"""Maximum number of entries (<url> or <sitemap>) per file.

The Sitemap protocol sets it at 50_000, but it also sets the max size of the
resulting file at 50 MiB. Following the initial Zenodo implementation, we
set it much lower than 50_000 so as to not have to check for generated size.

Following the initial Zenodo implementation, we use the same config for the
number of entries in the Sitemap Index and Sitemap files.
"""

SITEMAP_SECTIONS = []
"""Instances of `sitemap.SitemapSection` that will populate the Sitemap files."""

SITEMAP_ROOT_VIEW_ENABLED = True
"""Enable the `/sitemap.xml` endpoint serving the first sitemap index."""
