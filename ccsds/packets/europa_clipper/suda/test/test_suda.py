"""Unit tests for SUDA packet parser comparison."""
import os
import unittest

from spac_kit.parser import compare


class TestSudaCase: # pylint: disable=too-few-public-methods
    """Unit test class for SUDA packets."""
    def test_parse(self):
        """Test SUDA packet parsing, reference comparison."""
        local_dir = os.path.dirname(__file__)
        compare(local_dir, False, True, False, create_output=False)


if __name__ == "__main__":
    unittest.main()
