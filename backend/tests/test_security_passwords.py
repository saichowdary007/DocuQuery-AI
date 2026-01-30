import importlib.util
import sys
from pathlib import Path
import unittest


BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))


class TestPasswordHashing(unittest.TestCase):
    def test_password_hashing_long_input(self) -> None:
        if importlib.util.find_spec("passlib") is None:
            self.skipTest("passlib is not installed")
        from app.core.security import get_password_hash, verify_password

        long_password = "a" * 200
        hashed = get_password_hash(long_password)
        self.assertTrue(verify_password(long_password, hashed))

    def test_password_hashing_short_input(self) -> None:
        if importlib.util.find_spec("passlib") is None:
            self.skipTest("passlib is not installed")
        from app.core.security import get_password_hash, verify_password

        short_password = "docuquery@admin2025"
        hashed = get_password_hash(short_password)
        self.assertTrue(verify_password(short_password, hashed))


if __name__ == "__main__":
    unittest.main()

