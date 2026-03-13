import unittest

from misc.ica.database import InMemoryDatabase


class DatabaseTests(unittest.TestCase):

    def setUp(self):
        self.db = InMemoryDatabase()

    def test_set_and_get(self):
        self.assertEqual(self.db.set("user1", "name", "Alice"), "")
        self.assertEqual(self.db.set("user1", "age", "30"), "")
        self.assertEqual(self.db.get("user1", "name"), "Alice")
        self.assertEqual(self.db.get("user1", "age"), "30")

    def test_set_overwrite(self):
        self.assertEqual(self.db.set("user1", "name", "Alice"), "")
        self.assertEqual(self.db.set("user1", "name", "Bob"), "")
        self.assertEqual(self.db.get("user1", "name"), "Bob")

    def test_get_non_existent(self):
        self.assertEqual(self.db.get("user1", "field"), "")
        self.assertEqual(self.db.set("user1", "name", "Alice"), "")
        self.assertEqual(self.db.get("user1", "non_existent"), "")

    def test_delete(self):
        self.assertEqual(self.db.set("user1", "name", "Alice"), "")
        self.assertEqual(self.db.delete("user1", "name"), "true")
        self.assertEqual(self.db.get("user1", "name"), "")
        self.assertEqual(self.db.delete("user1", "name"), "false")
        self.assertEqual(self.db.delete("non_existent", "field"), "false")

    def test_scan(self):
        self.assertEqual(self.db.set("user1", "name", "Alice"), "")
        self.assertEqual(self.db.set("user1", "age", "30"), "")
        self.assertEqual(self.db.set("user1", "city", "NY"), "")
        self.assertEqual(self.db.set("user1", "abc", "123"), "")
        self.assertEqual(self.db.scan("user1"), "abc(123), age(30), city(NY), name(Alice)")
        self.assertEqual(self.db.scan("non_existent"), "")

    def test_scan_by_prefix(self):
        self.assertEqual(self.db.set("user1", "name", "Alice"), "")
        self.assertEqual(self.db.set("user1", "age", "30"), "")
        self.assertEqual(self.db.set("user1", "city", "NY"), "")
        self.assertEqual(self.db.set("user1", "abc", "123"), "")
        self.assertEqual(self.db.scan_by_prefix("user1", "a"), "abc(123), age(30)")
        self.assertEqual(self.db.scan_by_prefix("user1", "n"), "name(Alice)")
        self.assertEqual(self.db.scan_by_prefix("user1", "xyz"), "")

    def test_set_at_and_get_at(self):
        self.assertEqual(self.db.set_at("user1", "name", "Alice", timestamp=100), "")
        self.assertEqual(self.db.set_at("user1", "age", "30", timestamp=101), "")
        self.assertEqual(self.db.get_at("user1", "name", timestamp=102), "Alice")
        self.assertEqual(self.db.get_at("user1", "age", timestamp=103), "30")

    def test_get_at_non_existent(self):
        self.assertEqual(self.db.get_at("user2", "name", timestamp=100), "")
        self.assertEqual(self.db.get_at("user1", "non_existent", timestamp=101), "")

    def test_set_at_with_ttl_and_get_at(self):
        # The field is available between [100, 110)
        self.assertEqual(self.db.set_at_with_ttl("user1", "name", "Alice", timestamp=100, ttl=10), "")
        # At timestamp 105, the field should still be available
        self.assertEqual(self.db.get_at("user1", "name", timestamp=105), "Alice")
        # At timestamp 110, the field should have expired
        self.assertEqual(self.db.get_at("user1", "name", timestamp=110), "")
        # At timestamp 115, the field should still be expired
        self.assertEqual(self.db.get_at("user1", "name", timestamp=115), "")


if __name__ == "__main__":
    unittest.main()
