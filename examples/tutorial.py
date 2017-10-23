import sys

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
sys.path.extend(['.', '..'])

from pycparser import c_parser, c_ast, parse_file

# First we need to parse the input
parser = c_parser.CParser()
ast = parse_file('./c_files/tutorial.c')


# Let us have a look at how the program represents the AST
#ast.show()

# We can also show the first external definition of the AST
# ast.ext[0].show()

# The ast is a tree with nodes. Here each node is a superclass of Node with
# slots representing the different attributes or the children of the node.
# For example, Assignment has the attributes op, lvalue, rvalue, coord.
# - The op is the assignment operator, it could be '=', '+=', '++', etc...
# - The lvalue is the value on the left hand side of the assignment operator.
# - The rvalue is the value on the right hand side of the assignment operator.
# - The coord field represents the coordinates of the statement in the original C file.

# To explore and perform operations on the AST, we need to extend the NodeVisitor class.
# The NodeVisitor class has two methods, visit(Node) and generic_visit(Node).
# - To visit and perform actions on specific Nodes, you have to implement visit_XXX(self, node) methods
# that will visit the XXX type nodes.
# - For a node of type XXX, if no visit_XXX method has been specified, the generic_visit(self,node) is called.
# - Careful, by default the children of a node visited by a visit_XXX method will not be visited. If you want
# to visit the children of the XXX node, call generic_visit(XXX) on your node.

# The following class should implement a visitor for Assignments, and show the lvalue of the assignments
# class PrintLvalues(c_ast.NodeVisitor):
#     def visit_Assignment(self, assignment):
#         TODO
#
# print "Left values in the full AST"
# plv = PrintLvalues()
# plv.visit(ast)
# print ""


# Now we would like to print the left values only in function that are not the 'main' function.
# For each function, we want to print its name and then visit its body
# class DontVisitMainFunc(c_ast.NodeVisitor):
#     def visit_FuncDef(self, funcdef):
#         # We now what a funcdef Node looks like, so we can look for its name
#         if TODO:
#             print("In function %s :" % funcdef.decl.name)
#             # Now we want to continue visiting the node of the body using the left values printer
#             # visitor
#             PrintLvalues().visit(funcdef.body)
#
#
# print "Left values in functions that are not main"
# DontVisitMainFunc().visit(ast)


# You should get the idea by now: to visit an AST, you can implement different classes extending the
# NodeVisitor class and the in each class implement one or more visitor functions. Now let us
# try to do some dataflow analysis using visitors.

# First exercise: we want to have the set of variables written in a function. We assume that
# there are no side effects, and the only way to write in a variable is with an assignment.

# What is the effect of an assignment on the set of written variables? We just need to write in it.
# class WriteSetVisitor(c_ast.NodeVisitor):
#     def __init__(self, writeset):
#         if writeset is None:
#             self.writeset = set()
#         else:
#             self.writeset = writeset
#
#     def visit_Assignment(self, assignment):
        # The written variables are the variables on the left hand side
        # TODO


# Now we want to have the writeset of each function, we create another visitor
# class FuncDefsVisitor(c_ast.NodeVisitor):
#     def __init__(self):
#         self.writesets = {}
#
#     def visit_FuncDef(self, node):
#         TODO
#
# func_visit = FuncDefsVisitor()
# func_visit.visit(ast)
#
# for funcname, writeset  in func_visit.writesets.items():
#     print "\nin function %s :" % funcname
#     for lval in writeset:
#         print lval.name

# class ConstantPropagation(c_ast.NodeVisitor):
#     # We keep a map of variable names to constants
#     def __init__(self):
#         self.storage = {}
#     def visit_Decl(self, node):
#         TODO
#
# VisitDecl().visit(ast)