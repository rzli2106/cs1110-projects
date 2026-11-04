"""
The class definition for the class lab

The class Length should meet the specification outlined below. It has two 
(hidden) attributes accessible behind getters.  It has a __str__ method for 
object representation and a method for converting from one unit to another.

Initial skeleton by W. White (wmw2)

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


class Length(object):
    """
    A class representing a measurement of length.
    
    Length is defined as a numerical value plus a unit of measurement.
    """
    # MUTABLE ATTRIBUTES
    # Attribute _value: The measured length
    #Invariant: _value is a float
    #
    # IMMUTABLE ATTRIBUTES
    # Attribute _unit: The unit of measurement
    #Invariant: _unit is a string and either 'ft' or 'm'
    
    # GETTERS AND SETTERS GO HERE
    def getUnit(self):
        return self._unit
    
    def getValue(self):
        return self._value
    
    def setValue(self, v):
        assert type(v) == float 
        self._value = v
        
    # INITIALIZER
    def __init__(self, v, u = 'ft'):
        assert type(v) is float
        assert type(u) is str
        assert u == 'ft' or u == 'm'
        self._value = v
        self._unit = u
    
    # __str__ METHOD
    def __str__(self):
        return str(self._value) + ' ' + str(self._unit)


    # Method measure
    def measure(self, unit):
        assert type(unit) == str
        assert unit == 'ft' or unit == 'm'
        
        if unit == self.getUnit():
            return self.getValue()
            
        if unit == 'm': 
            return self.getValue() * 0.3048
        else:
            return self.getValue() / 0.3048

