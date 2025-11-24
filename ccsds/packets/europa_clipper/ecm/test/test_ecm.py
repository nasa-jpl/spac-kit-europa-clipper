"""Unit tests for Europa Clipper ECM packets."""
import os
import unittest

from spac_kit.parser import compare


class TestECMCase: # pylint: disable=too-few-public-methods
    """Unit test class for ECM packets."""
    def test_parse(self):
        """Test ECM packet parsing, reference comparison."""
        local_dir = os.path.dirname(__file__)
        compare(local_dir, True, True, False, create_output=False)


if __name__ == "__main__":
    unittest.main()
