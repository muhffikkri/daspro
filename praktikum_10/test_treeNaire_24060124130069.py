import unittest
from treeNaire_24060124130069 import searchXTree, makePN

class TestTreeNaire(unittest.TestCase):

    def setUp(self):
        self.tree = makePN("A", 
            [
                makePN("B", 
                    [
                        makePN("D", []), 
                        makePN("E", [])
                    ]),
                makePN("C",
                    [
                        makePN("F", 
                            [
                                makePN("G", []),
                            ])
                    ])
            ])

    def test_searchXTree_found(self):
        self.assertTrue(searchXTree("A", self.tree))
        self.assertTrue(searchXTree("B", self.tree))
        self.assertTrue(searchXTree("C", self.tree))
        self.assertTrue(searchXTree("D", self.tree))
        self.assertTrue(searchXTree("E", self.tree))
        self.assertTrue(searchXTree("F", self.tree))
        self.assertTrue(searchXTree("G", self.tree))

    def test_searchXTree_not_found(self):
        self.assertFalse(searchXTree("Z", self.tree))
        self.assertFalse(searchXTree("H", self.tree))
        self.assertFalse(searchXTree("I", self.tree))

if __name__ == '__main__':
    unittest.main()