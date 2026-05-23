# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-FileCopyrightText: 2025 Northwestern University.
# SPDX-License-Identifier: MIT

"""Sitemap indices and sitemaps for InvenioRDM."""

from . import config


class InvenioSitemap:
    """Extensions for invenio-sitemap."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        app.extensions["invenio-sitemap"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith("SITEMAP_"):
                app.config.setdefault(k, getattr(config, k))
