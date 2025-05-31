import unittest
from app import RecentlyUsedList

class TestRecentlyUsedList(unittest.TestCase):

    def test_only_string_allowed(self):
        new_list = RecentlyUsedList()
        with self.assertRaises(TypeError) as context:
            new_list.add_item(1)
        self.assertEqual(str(context.exception), "Only Strings Allowed")

    def test_recently_added_item_first(self):
        new_list = RecentlyUsedList()
        new_list.add_item("John")
        new_list.add_item("Jane")
        new_list.add_item("Shubham")
        self.assertEqual(new_list.lookup_item(0), "Shubham")

    def test_lookup_by_index(self):
        new_list = RecentlyUsedList()
        new_list.add_item("Shubham")
        new_list.add_item("John")
        new_list.add_item("Jane")
        self.assertEqual(new_list.lookup_item(2), "Shubham")
        self.assertEqual(new_list.lookup_item(1), "John")
        self.assertEqual(new_list.lookup_item(0), "Jane")

    def test_duplicate_moved_out(self):
        new_list = RecentlyUsedList()
        new_list.add_item("Shubham")
        new_list.add_item("John")
        new_list.add_item("Shubham")
        self.assertEqual(new_list.lookup_item(0), "Shubham")
        self.assertEqual(new_list.get_length(), 2)

    def test_initial_empty_list(self):
        new_list = RecentlyUsedList()
        self.assertEqual(new_list.get_length(), 0)

    def test_size_limit(self):
        new_list = RecentlyUsedList(size_limit=3)
        new_list.add_item("Shubham")
        new_list.add_item("Jane")
        new_list.add_item("Jack")
        new_list.add_item("John")
        self.assertEqual(new_list.get_length(), 3)
        self.assertEqual(new_list.lookup_item(2), "Jane")

    def test_empty_string_not_allowed(self):
        new_list = RecentlyUsedList()
        with self.assertRaises(ValueError) as context:
            new_list.add_item("")
        self.assertEqual(str(context.exception), "Empty String Not Allowed")

    def test_lookup_within_bounds(self):
        new_list = RecentlyUsedList()
        new_list.add_item("Shubham")
        new_list.add_item("John")
        new_list.add_item("Jane")
        with self.assertRaises(IndexError) as context:
            new_list.lookup_item(3)
        self.assertEqual(str(context.exception), "Lookup Index Out Of Range")

    def test_negative_index_lookup_not_allowed(self):
        new_list = RecentlyUsedList()
        new_list.add_item("Shubham")
        new_list.add_item("John")
        new_list.add_item("Jane")
        with self.assertRaises(IndexError) as context:
            new_list.lookup_item(-1)
        self.assertEqual(str(context.exception), "Negative Lookup Not Allowed")

    def test_default_size_limit(self):
        new_list = RecentlyUsedList()
        new_list.add_item("Shubham")
        new_list.add_item("John")
        new_list.add_item("Jane")
        new_list.add_item("Jack")
        new_list.add_item("Jake")
        new_list.add_item("James")
        self.assertEqual(new_list.get_length(), 5)
        self.assertEqual(new_list.lookup_item(4), "John")

    def test_non_sizable_list(self):
        new_list = RecentlyUsedList(size_limit=None)
        new_list.add_item("Shubham")
        new_list.add_item("John")
        new_list.add_item("Jane")
        new_list.add_item("Jack")
        new_list.add_item("Jake")
        new_list.add_item("James")

        self.assertEqual(new_list.get_length(), 6)
        self.assertEqual(new_list.lookup_item(5), "Shubham")

if __name__ == "__main__":
    unittest.main()
    