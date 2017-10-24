import sys
import unittest
from pycparser import parse_file
import minic.c_ast_to_minic as ctoc
import minic.minic_ast as mast

sys.path.insert(0, '..')

class Test_c_ast_to_minic(unittest.TestCase):
    def test_parse_and_convert(self):
        fullc_ast = parse_file('./c_files/minic.c')
        converted = ctoc.t(fullc_ast)
        self.failUnless(isinstance(converted, mast.FileAST))

