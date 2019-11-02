import sys
import unittest
import logging
from hruid.adjectives import adjectives
from hruid.verbs import verbs
from hruid.adverbs import adverbs

wordlist_specs = [
    {"name": "adjectives", "data": adjectives, "length": 128},
    {"name": "nouns", "data": adjectives, "length": 128},
    {"name": "verbs", "data": verbs, "length": 128},
    {"name": "adverbs", "data": adverbs, "length": 64},
]

log = logging.getLogger("testLogger")
logging.basicConfig(stream=sys.stderr, level=logging.INFO)


class TestWordLists(unittest.TestCase):
    def test_list_length(self):
        """
        Check the length of the each word list is correct
        """
        for wordlist in wordlist_specs:
            name = wordlist["name"]
            expected_length = wordlist["length"]
            err_msg = f"Number of words in list '{name}' does not match its specification of {expected_length}"

            actual_length = len(wordlist["data"])
            if expected_length is None:
                log.info(
                    f"The number of words in the list '{name}' is {actual_length} (no specfication set)"
                )
                self.assertTrue(True)
            else:
                self.assertEqual(
                    actual_length, expected_length, err_msg,
                )

    def test_word_format(self):
        """
        Ensure all words are lowercase for every word list
        """
        for wordlist in wordlist_specs:
            for word in wordlist:
                err_msg = f"The word '{word}' in the list '{wordlist['name']}' should be lowercase"
                self.assertTrue(word.islower(), err_msg)

    def test_for_duplicates(self):
        """
        Check each list for duplicates
        """
        for wordlist in wordlist_specs:
            err_msg = f"There are duplicates in the list '{wordlist['name']}'"
            self.assertEqual(len(set(wordlist)), len(wordlist), err_msg)


if __name__ == "__main__":
    unittest.main()
