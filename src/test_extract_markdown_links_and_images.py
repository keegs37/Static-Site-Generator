from extract_markdown_links_and_images import extract_markdown_images, extract_markdown_links
import unittest




class TestExtractMarkdownImages(unittest.TestCase):
    # --- Happy paths ---

    def test_images_single(self):
        text = "Here is an image: ![alt text](https://example.com/image.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [("alt text", "https://example.com/image.png")],
        )

    def test_images_multiple(self):
        text = "![one](https://img/1.png) and ![two](https://img/2.png)"
        self.assertEqual(
            extract_markdown_images(text),
            [("one", "https://img/1.png"), ("two", "https://img/2.png")],
        )

    # --- Mixed content: desired behavior vs current implementation ---

    @unittest.expectedFailure
    def test_images_mixed_with_links_should_return_only_images(self):
        text = "![logo](https://img/logo.png) and [site](https://example.com)"
        # Desired: only the image tuple, not the link
        self.assertEqual(
            extract_markdown_images(text),
            [("logo", "https://img/logo.png")],
        )

    # --- Error & edge cases ---

    def test_images_raises_when_none_present(self):
        text = "No markdown images here."
        with self.assertRaises(Exception) as ctx:
            extract_markdown_images(text)
        self.assertIn("image", str(ctx.exception).lower())

    def test_images_mismatch_more_alts_than_urls_raises_index_error(self):
        # Two bracketed alts but only one URL -> current code IndexError
        text = "![one](https://img/1.png) ![two]"
        with self.assertRaises(IndexError):
            extract_markdown_images(text)

    def test_images_mismatch_more_urls_than_alts_truncates_silently(self):
        text = "![one](https://img/1.png) (https://extra.com/ignored)"
        self.assertEqual(
            extract_markdown_images(text),
            [("one", "https://img/1.png")],
        )

    @unittest.expectedFailure
    def test_images_urls_with_parentheses_in_path(self):
        text = "![plot](https://example.com/img/foo_(bar).png)"
        self.assertEqual(
            extract_markdown_images(text),
            [("plot", "https://example.com/img/foo_(bar).png")],
        )

    @unittest.expectedFailure
    def test_images_non_markdown_brackets_parens_should_not_match(self):
        text = "This is [not a link] (not-a-url) just prose."
        self.assertEqual(extract_markdown_images(text), [])


class TestExtractMarkdownLinks(unittest.TestCase):
    # --- Happy paths ---

    def test_links_single(self):
        text = "Click [Example](https://example.com) for details."
        self.assertEqual(
            extract_markdown_links(text),
            [("Example", "https://example.com")],
        )

    def test_links_multiple(self):
        text = "[A](https://a.com) then [B](https://b.com)"
        self.assertEqual(
            extract_markdown_links(text),
            [("A", "https://a.com"), ("B", "https://b.com")],
        )

    # --- Mixed content: desired vs current behavior ---

    @unittest.expectedFailure
    def test_links_mixed_with_images_should_return_only_links(self):
        text = "![logo](https://img/logo.png) and [site](https://example.com)"
        self.assertEqual(
            extract_markdown_links(text),
            [("site", "https://example.com")],
        )

    # --- Error & edge cases ---

    def test_links_raises_when_none_present(self):
        text = "No markdown links here."
        with self.assertRaises(Exception) as ctx:
            extract_markdown_links(text)
        # Current implementation says "image(s)" even for links
        self.assertIn("image", str(ctx.exception).lower())

    @unittest.expectedFailure
    def test_links_non_markdown_brackets_parens_should_not_match(self):
        text = "This is [not a link] (not-a-url) just prose."
        self.assertEqual(extract_markdown_links(text), [])


if __name__ == "__main__":
    unittest.main()
