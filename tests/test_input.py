import unittest
from app.io.input import read_from_file_builtin, read_from_file_pandas

class TestInputFunctions(unittest.TestCase):
    def test_read_from_file_builtin_empty(self):
        """Test reading an empty file."""
        with open("data/input.txt", "w") as f:
            f.write("")
        self.assertEqual(read_from_file_builtin(), "")

    def test_read_from_file_builtin_content(self):
        """Test reading a file with content."""
        with open("data/input.txt", "w") as f:
            f.write("Test")
        self.assertEqual(read_from_file_builtin(), "Test")

    def test_read_from_file_builtin_exists(self):
        """Test that reading from file returns something."""
        with open("data/input.txt", "w") as f:
            f.write("Something")
        self.assertIsNotNone(read_from_file_builtin())

        def test_read_from_file_pandas_empty(self):
            """Test reading an empty CSV file."""
            with open("data/input.csv", "w") as f:
                f.write("col1,col2\n")
            self.assertTrue("Empty DataFrame" in read_from_file_pandas())

        def test_read_from_file_pandas_content(self):
            """Test reading a CSV file with content."""
            with open("data/input.csv", "w") as f:
                f.write("col1,col2\n1,2")
            self.assertTrue("col1" in read_from_file_pandas())

        def test_read_from_file_pandas_exists(self):
            """Test that reading from CSV returns something."""
            with open("data/input.csv", "w") as f:
                f.write("col1,col2\n1,2")
            self.assertIsNotNone(read_from_file_pandas())

if __name__ == "__main__":
    unittest.main()