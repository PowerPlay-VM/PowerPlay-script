from lang_builtin import *

class Base_node():
    def __init__(self):
        self.subnode = None

    def execute(self):
        pass

class Statements_node():
    def __init__(self,left,right):
        super().__init__()

        self.left = left
        self.right = right

    def execute(self):
        left = self.left.execute()
        right = self.right.execute()

class Value_node(Base_node):
    def __init__(self,value):
        super().__init__()

        self.value = value

    def execute(self):
        return self.value

class Id_node(Base_node):
    def __init__(self,name):
        super().__init__()

        self.name = name

    def execute(self):
        return variables[self.name]

class Add_node(Base_node):
    def __init__(self,left,right):
        super().__init__()

        self.left = left
        self.right = right

    def execute(self):
        left = self.left.execute()
        right = self.right.execute()

        return left + right
    
class Sub_node(Base_node):
    def __init__(self,left,right):
        super().__init__()

        self.left = left
        self.right = right

    def execute(self):
        left = self.left.execute()
        right = self.right.execute()

        return left - right
    
class Mul_node(Base_node):
    def __init__(self,left,right):
        super().__init__()

        self.left = left
        self.right = right

    def execute(self):
        left = self.left.execute()
        right = self.right.execute()

        return left * right
    
class Div_node(Base_node):
    def __init__(self,left,right):
        super().__init__()

        self.left = left
        self.right = right

    def execute(self):
        left = self.left.execute()
        right = self.right.execute()

        return left / right
    
class Assign_node(Base_node):
    def __init__(self,name,value):
        super().__init__()

        self.name = name
        self.value = value

    def execute(self):
        name = self.name
        value = self.value.execute()
        variables[name] = value

class Equal_node(Base_node):
    def __init__(self,left,right):
        super().__init__()

        self.left = left
        self.right = right

    def execute(self):

        left = self.left.execute()
        right = self.right.execute()

        return left == right
    
class Not_equal_node(Base_node):
    def __init__(self,left,right):
        super().__init__()

        self.left = left
        self.right = right

    def execute(self):

        left = self.left.execute()
        right = self.right.execute()

        return left != right

class Little_than_node(Base_node):
    def __init__(self,left,right):
        super().__init__()

        self.left = left
        self.right = right

    def execute(self):

        left = self.left.execute()
        right = self.right.execute()

        return left < right

class Little_equal_node(Base_node):
    def __init__(self,left,right):
        super().__init__()

        self.left = left
        self.right = right

    def execute(self):

        left = self.left.execute()
        right = self.right.execute()

        return left <= right

class Greater_than_node(Base_node):
    def __init__(self,left,right):
        super().__init__()

        self.left = left
        self.right = right

    def execute(self):

        left = self.left.execute()
        right = self.right.execute()

        return left > right
    
class Greater_equal_node(Base_node):
    def __init__(self,left,right):
        super().__init__()

        self.left = left
        self.right = right

    def execute(self):

        left = self.left.execute()
        right = self.right.execute()

        return left >= right
    
class Call_node(Base_node):
    def __init__(self,name,args):
        super().__init__()

        self.name = name
        self.args = args

    def execute(self):
        name = self.name
        args = self.args.execute()

        functions[name](args)

class If_node(Base_node):
    def __init__(self,condition,statement,else_statement):
        super().__init__()

        self.condition = condition
        self.statement = statement
        self.else_statement = else_statement

    def execute(self):

        condition = self.condition.execute()

        if condition:
            self.statement.execute()

        else:
            if self.else_statement != None:
                self.else_statement.execute()
      
