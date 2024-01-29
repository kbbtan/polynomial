class X:
    """ This class represents the X variable in a polynomial.
    """
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    """ This class represents any standalone integers in a polynomial.
    """
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    """ This class represents adding two elements in a polynomial together.
    """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
class Subtract:
    """ This class represents subtracting element p2 from element p1 in a polynomial.
    """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)

class Mul:
    """ This class represents multiplying two elements in a polynomial together.
    """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        # Respect order of operations when both arguments include + / -.
        if isinstance(self.p1, (Add, Subtract)) and isinstance(self.p2, (Add, Subtract)):
            return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"

        # Respect order of operations when only p1 includes + / -.
        if isinstance(self.p1, (Add, Subtract)):
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        
        # Respect order of operations when only p2 includes + / -.
        if isinstance(self.p2, (Add, Subtract)):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        
        # Otherwise, we can simply return without any brackets.
        return repr(self.p1) + " * " + repr(self.p2)

class Div:
    """ This class represents dividing element p1 by element p2 in a polynomial.
    """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        # Respect order of operations when both arguments include + / -.
        if isinstance(self.p1, (Add, Subtract)) and isinstance(self.p2, (Add, Subtract)):
            return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"

        # Respect order of operations when only p1 includes + / -.
        if isinstance(self.p1, (Add, Subtract)):
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        
        # Respect order of operations when only p2 includes + / -.
        if isinstance(self.p2, (Add, Subtract)):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        
        # Otherwise, we can simply return without any brackets.
        return repr(self.p1) + " / " + repr(self.p2)

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)