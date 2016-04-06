import os
import sys
try:
    import unittest2
except ImportError:
    import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import vbox


class TestWord(unittest.TestCase):
    def test_init(self):
        w = vbox.Word('anime')
        self.assertEqual(w.string, 'anime')


@patch('vbox.Word')
class TestVoice(unittest.TestCase):
    def test_init(self, mock_word):
        m = mock_word()
        m.freq = 1
        v = vbox.Voice('good book', {
            'who\'s': m,
            'a': m,
            'good': m,
            'boy': m,
        })
        self.assertEqual(v.name, 'good book')


@patch('vbox.Word')
class TestContext(unittest.TestCase):
    def test_init(self, mock_word):
        m = mock_word()
        mock_dict = {
            'who\'s': m,
            'a': m,
            'good': m,
            'boy': m,
        }
        c = vbox.Context(mock_dict, [m, m, m, m], [m, m, m, m, m])
        self.assertEqual(c.prev_ngrams_wt, [8.0, 4.0, 2.0, 1.0])


class TestVoicebox(unittest.TestCase):
    def test_init(self):
        v = vbox.Voicebox()
        self.assertEqual(v.vision, 2)

    def test_fileadd(self):
        v = vbox.Voicebox()
        v.addVoiceFromFile('howl')
        self.assertIn('1. howl', v.voices)


class TestWriter(unittest.TestCase):
    def test_write_none(self):
        w = vbox.Writer()
        w.write()


if __name__ == '__main__':
    unittest.main()
