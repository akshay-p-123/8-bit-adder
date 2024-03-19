class Adders:

    #a, b, and c are one bit each

    @staticmethod
    def half_adder_without_carry(a, b):
        return a ^ b
    
    @staticmethod
    def full_adder_without_carry(a, b, c):
        return (a ^ b) ^ c
    
    @staticmethod
    def full_adder_with_carry(a, b, c):
        sum = Adders.full_adder_without_carry(a, b, c)
        carry = (a & b) | ((a ^ b) & c)
        return (sum, carry)