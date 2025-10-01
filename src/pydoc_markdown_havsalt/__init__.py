"""
Plugin for `pydoc-markdown`
===========================

This plugin offers additional features for documenting with the
well-written `pydoc-markdown` tool.

Often used in `Havsalt`'s projects.
"""

__all__ = [
    "RuffMarkdownRenderer",
]

from .renderers import RuffMarkdownRenderer
