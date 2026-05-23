# SPDX-FileCopyrightText: 2025 CERN.
# SPDX-FileCopyrightText: 2025 Northwestern University.
# SPDX-License-Identifier: MIT


from invenio_sitemap.cache import BaseSitemapCache


class FakeSitemapCache(BaseSitemapCache):
    """Fake cache for testing purposes."""

    prefix = "fake"


def test_base_sitemap_cache_iterate_keys(empty_cache):
    cache_fake = FakeSitemapCache(empty_cache)
    cache_fake.set(0, "foo")  # stored object shape doesn't matter
    cache_fake.set(1, "bar")
    cache_fake.set("baz", "baz")

    keys = list(cache_fake.iterate_keys())

    assert [0, 1] == keys
