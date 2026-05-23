# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-FileCopyrightText: 2025 Northwestern University.
# SPDX-License-Identifier: MIT

"""Sitemap (+index) section interface."""

import abc


class SitemapSection(abc.ABC):
    """Parent class to any Sitemap section."""

    @abc.abstractmethod
    def iter_entities(self):
        """Iterate entities that will be converted to a Sitemap entry."""

    @abc.abstractmethod
    def to_dict(self, entity):
        """Converts an entity to a Sitemap dict entry.

        Done this way because:
        - different entities may iterated, and conversion depends on kind of entity
        - Sitemap extensions may support new fields
        - Jinja can easily interface with dict

        Further reading

        See https://sitemaps.org/protocol.html for potentials fields.
        See https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap#additional-notes-about-xml-sitemaps
        for how Google deals with Sitemaps.

        The only required field is "loc". InvenioRDM modules should implement
        "lastmod". Google ignores "priority" and "changefreq" fields so InvenioRDM
        modules shouldn't bother with them by default.

        "lastmod" MUST follow https://www.w3.org/TR/NOTE-datetime , but we provide a
        helper function below for use by implementations.
        """
