import unittest
from copystatic import (
    extract_title
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_extract_title_present(self):
        md = """
#     This is a **bolded** title

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        title = extract_title(md)
        self.assertEqual(
            title,
            "This is a **bolded** title",
        )
    
    def test_no_title_err(self):
        md = """
This is a **bolded** title

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        with self.assertRaises(Exception):
            title = extract_title(md)
        
