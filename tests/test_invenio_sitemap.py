# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 CERN.
# Copyright (C) 2025 Northwestern University.
#
# invenio-sitemap is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from flask import Flask

from invenio_sitemap import InvenioSitemap


def test_version():
    """Test version import."""
    from invenio_sitemap import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioSitemap(app)
    assert "invenio-sitemap" in app.extensions

    app = Flask("testapp")
    ext = InvenioSitemap()
    assert "invenio-sitemap" not in app.extensions
    ext.init_app(app)
    assert "invenio-sitemap" in app.extensions


def test_config_defaults():
    """Test that default configuration values are set correctly."""
    app = Flask("testapp")
    ext = InvenioSitemap(app)

    assert app.config.get("SITEMAP_ROOT_VIEW_ENABLED") is True
    assert app.config.get("SITEMAP_MAX_ENTRY_COUNT") == 10000
    assert app.config.get("SITEMAP_SECTIONS") == []


def test_config_override():
    """Test that configuration can be overridden."""
    app = Flask("testapp")
    app.config["SITEMAP_ROOT_VIEW_ENABLED"] = False
    app.config["SITEMAP_MAX_ENTRY_COUNT"] = 5000

    ext = InvenioSitemap(app)

    assert app.config["SITEMAP_ROOT_VIEW_ENABLED"] is False
    assert app.config["SITEMAP_MAX_ENTRY_COUNT"] == 5000
