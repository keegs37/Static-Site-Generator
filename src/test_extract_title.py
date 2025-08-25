import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_simple_h1_at_start(self):
        self.assertEqual(extract_title("# My Title"), "My Title")

    def test_includes_entire_remainder_of_doc_after_hash(self):
        md = "# My Title\nThis is the body paragraph."
        # Because the function splits on whitespace and rejoins everything
        # after the first '#' token, it will include the body too.
        self.assertEqual(extract_title(md), "My Title This is the body paragraph.")

    def test_title_normalizes_whitespace(self):
        self.assertEqual(extract_title("   #    Spaced    Out   "), "Spaced Out")

    def test_hash_not_separate_token_is_ignored(self):
        # '#Title' is a single token, not equal to '#', so this should raise.
        with self.assertRaises(Exception) as ctx:
            extract_title("#Title")
        self.assertIn("Title not found", str(ctx.exception))

    def test_no_hash_raises(self):
        with self.assertRaises(Exception) as ctx:
            extract_title("No title here, just text.")
        self.assertIn("Title not found", str(ctx.exception))

    def test_first_hash_wins_when_multiple(self):
        md = "# First Title\nSome text\n# Second Title"
        # Function returns everything after the FIRST '#' token, including the next '#'
        self.assertEqual(extract_title(md), "First Title Some text # Second Title")

    def test_hash_in_middle_of_text(self):
        md = "Intro text before\n# Actual Title\nMore"
        self.assertEqual(extract_title(md), "Actual Title More")


if __name__ == "__main__":
    unittest.main()
