import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class LiteRedirectTests(unittest.TestCase):
    def test_redirects_to_full_source_in_lite_mode(self):
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertIn("https://superhedgehoger.github.io/Geomap-app/", page)
        self.assertIn("variant=lite", page)
        self.assertIn("target.searchParams.set('variant', 'lite')", page)

    def test_entry_does_not_load_a_second_application_copy(self):
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        self.assertNotIn('src="script.js"', page)
        self.assertNotIn('href="style.css"', page)


if __name__ == "__main__":
    unittest.main()
