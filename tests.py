import minecraft_with_python as mcwpy
import unittest
import os

class Tests(unittest.TestCase):
    def test_class_datapack_path(self):
        # Check that the path always ends with a path separator ("/") or nothing ("")
        self.assertEqual(mcwpy.Datapack(path='').path, '')
        self.assertEqual(mcwpy.Datapack(path=None).path, '')
        self.assertEqual(mcwpy.Datapack(path='~/home').path[-1], os.path.sep)
        self.assertEqual(mcwpy.Datapack(path='~/home/').path[-2:], f'e{os.path.sep}')

    def test_class_datapack_workspaces(self):
        self.assertIsInstance(mcwpy.Datapack(workspaces=[]).workspaces, list)

    def test_class_workspace_title(self):
        self.assertEqual(mcwpy.Workspace(title='MCWPY is AmAzInG').title, 'mcwpy_is_amazing')
        self.assertEqual(mcwpy.Workspace(title='mcwpy_is_amazing').title, 'mcwpy_is_amazing')
        self.assertEqual(mcwpy.Workspace(title='mcwpy-is-amazing').title, 'mcwpy-is-amazing')
        self.assertEqual(mcwpy.Workspace(title=None).title, 'mcwpy')
        self.assertEqual(mcwpy.Workspace(title='').title, 'mcwpy')
        self.assertEqual(mcwpy.Workspace().title, 'mcwpy')

    def test_class_workspace_content(self):
        self.assertIsInstance(mcwpy.Workspace(content=None).content, dict)
        self.assertIsInstance(mcwpy.Workspace(content={}).content, dict)

if __name__ == '__main__':
    unittest.main()
