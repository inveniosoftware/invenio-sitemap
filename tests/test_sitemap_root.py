# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 CERN.
# Copyright (C) 2025 Northwestern University.
#
# invenio-sitemap is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Tests for the /sitemap.xml endpoint."""

import xmlschema

from invenio_sitemap.cache import SitemapIndexCache


def test_sitemap_root_enabled_by_default(client, primed_cache):
    """Test that /sitemap.xml is enabled by default and returns first index page."""
    resp = client.get("/sitemap.xml")
    assert resp.status_code == 200
    assert resp.content_type == "application/xml"

    # Verify it contains both sitemap index entries
    assert b"<loc>https://127.0.0.1:5000/sitemap_0.xml</loc>" in resp.data
    assert b"<loc>https://127.0.0.1:5000/sitemap_1.xml</loc>" in resp.data


def test_sitemap_root_disabled_when_configured(
    client, primed_cache, set_app_config_fn_scoped
):
    """Test that /sitemap.xml returns 404 when explicitly disabled."""
    set_app_config_fn_scoped({"SITEMAP_ROOT_VIEW_ENABLED": False})

    resp = client.get("/sitemap.xml")
    assert resp.status_code == 404


def test_sitemap_root_empty_cache(client, empty_cache):
    """Test that /sitemap.xml returns 404 when first index page is not cached."""

    resp = client.get("/sitemap.xml")
    assert resp.status_code == 404


def test_sitemap_root_only_first_page(client, empty_cache):
    """Test that /sitemap.xml only returns the first index page."""

    # Manually populate cache with multiple index pages
    sitemap_index_cache = SitemapIndexCache(empty_cache)

    # Add first index page
    sitemap_index_cache.set(
        0,
        [
            {
                "loc": "https://127.0.0.1:5000/sitemap_0.xml",
                "lastmod": "2025-01-01T00:00:00Z",
            },
            {
                "loc": "https://127.0.0.1:5000/sitemap_1.xml",
                "lastmod": "2025-01-02T00:00:00Z",
            },
        ],
    )

    # Add second index page (should be ignored)
    sitemap_index_cache.set(
        1,
        [
            {
                "loc": "https://127.0.0.1:5000/sitemap_2.xml",
                "lastmod": "2025-01-03T00:00:00Z",
            },
            {
                "loc": "https://127.0.0.1:5000/sitemap_3.xml",
                "lastmod": "2025-01-04T00:00:00Z",
            },
        ],
    )

    resp = client.get("/sitemap.xml")
    assert resp.status_code == 200

    # Verify only sitemaps from first index page are included
    assert b"<loc>https://127.0.0.1:5000/sitemap_0.xml</loc>" in resp.data
    assert b"<loc>https://127.0.0.1:5000/sitemap_1.xml</loc>" in resp.data
    # These should NOT be included (from second index page)
    assert b"<loc>https://127.0.0.1:5000/sitemap_2.xml</loc>" not in resp.data
    assert b"<loc>https://127.0.0.1:5000/sitemap_3.xml</loc>" not in resp.data
