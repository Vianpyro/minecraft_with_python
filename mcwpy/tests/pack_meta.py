# -*- coding: ascii -*-
from mcwpy import Pack_Meta, get_minecraft_pack_version
import unittest


class TestDatapack(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.example_pack_meta = Pack_Meta(author='MCWPy', description='An amazing Minecraft datapack!', minecraft_version=7)

    def test_datapack_default_values(self):
        self.assertEqual(Pack_Meta().meta['description'], 'A Minecraft datapack.')
        self.assertEqual(Pack_Meta().meta['pack_format'], get_minecraft_pack_version('latest'))

    def test_datapack_default_instances(self):
        self.assertIsInstance(Pack_Meta(), Pack_Meta)
        self.assertIsInstance(Pack_Meta()(), str)
        self.assertIsInstance(Pack_Meta().__call__(), str)
        self.assertIsInstance(Pack_Meta().__repr__(), str)

    def test_datapack_equal_values(self):
        self.assertEqual(Pack_Meta()(), Pack_Meta().__call__())
        self.assertEqual(Pack_Meta().__call__(), Pack_Meta().__repr__())
        self.assertEqual(self.example_pack_meta(), self.example_pack_meta.__call__())
        self.assertEqual(self.example_pack_meta.__call__(), self.example_pack_meta.__repr__())


if __name__ == '__main__':
    unittest.main()
