import unittest

from dumpit.coloring import NoColors, TerminalColors


class TestColoring(unittest.TestCase):

    def setUp(self):
        pass

    def test_no_colors(self):
        coloring = NoColors()
        string = 'foo_bar'

        self.assertEqual(
            coloring.style(
                string, fg='red', bg='red'), string)

    def test_terminal_colors(self):
        coloring = TerminalColors()
        string = 'foo_bar'
        colored_string = '\x1b[31m\x1b[41mfoo_bar\x1b[0m'

        self.assertEqual(
            coloring.style(
                string, fg='red', bg='red'), colored_string)
