# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-FileCopyrightText: 2025 Northwestern University.
# SPDX-FileCopyrightText: 2026 TU Wien.
# SPDX-License-Identifier: MIT

"""Fake Sitemap Sections."""

from datetime import datetime, timezone

import pendulum

from invenio_sitemap.sitemap import SitemapSection
from invenio_sitemap.utils import format_to_w3c


class FakeSitemapSection1(SitemapSection):
    """Fake SitemapSection 1."""

    def iter_entities(self):
        """Iterate over objects of concern."""
        return [
            {
                "id": "foo",
                "updated": datetime(2025, 2, 2, tzinfo=timezone.utc),
            },
            {
                "id": "bar",
                "updated": pendulum.instance(datetime(2025, 2, 1, 22), tz="US/Pacific"),
            },
            {
                "id": "baz",
                "updated": datetime(2025, 2, 1, tzinfo=timezone.utc),
            },
        ]

    def to_dict(self, entity):
        """To dict used in sitemap."""
        return {
            "loc": "https://127.0.0.1:5000/" + entity["id"],
            "lastmod": format_to_w3c(entity["updated"]),
        }


class FakeSitemapSection2(SitemapSection):
    """Fake SitemapSection 2."""

    def iter_entities(self):
        """Iterate over objects of concern."""
        return [
            {
                "identifier": "barun",
                "modified": datetime(2025, 1, 1, tzinfo=timezone.utc),
            },
        ]

    def to_dict(self, entity):
        """To dict used in Sitemap."""
        return {
            "loc": "https://127.0.0.1:5000/" + entity["identifier"],
            "lastmod": format_to_w3c(entity["modified"]),
        }
