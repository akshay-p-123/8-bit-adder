from adders import Adders

#assuming inputs are valid
inp1 = input("enter an 8-bit binary number: ")
inp2 = input("enter another 8-bit binary number: ")

#turn big-endian inputs into little-endian lists with a placeholder at the beginning
#so list indexing matches the indexing in the boolean calculations and schematic
n1 = [int(i) for i in inp1] + [-1]
n2 = [int(i) for i in inp2] + [-1]
n1, n2 = n1[::-1], n2[::-1]


g = [-1] + [n1[i] & n2[i] for i in range(1,9)] #little-endian list of 'generate' bits
p = [-1] + [n1[i] ^ n2[i] for i in range(1,9)] #little-endian list of 'propagate' bits


s = [-1, 0, 0, 0, 0, 0, 0, 0, 0] #little-endian list of sum bits with placeholder


'''carry calculations & sums'''

#c1-c3 and s1-s3 all occur simultaneously
c1 = g[1]
c2 = g[2] | (p[2] & g[1])
c3 = g[3] | (p[3] & g[2]) | (p[3] & p[2] & g[1])

s[1] = Adders.half_adder_without_carry(n1[1], n2[1])
s[2] = Adders.full_adder_without_carry(n1[2], n2[2], c1)
s[3] = Adders.full_adder_without_carry(n1[3], n2[3], c2)

#last carry bit 'ripples' over to full adder to avoid lookahead-carry logic getting too complex
#this method maintains the majority of the speed of lookahead-carry
s[4], c4 = Adders.full_adder_with_carry(n1[4], n2[4], c3)

#c5-c8 calculations treat c4 like c0
#c5-c8 and s5-s8 all occur simultaneously
c5 = g[5] | (p[5] & c4)
c6 = g[6] | (p[6] & g[5]) | (p[6] & p[5] & c4)
c7 = g[7] | (p[7] & g[6]) | (p[7] & p[6] & g[5]) | (p[7] & p[6] & p[5] & c4)

s[5] = Adders.full_adder_without_carry(n1[5], n2[5], c4)
s[6] = Adders.full_adder_without_carry(n1[6], n2[6], c5)
s[7] = Adders.full_adder_without_carry(n1[7], n2[7], c6)

#same logic as c4
s[8], c8 = Adders.full_adder_with_carry(n1[8], n2[8], c7)


output = str(c8)
#converts s to big-endian
for i in range(-1, -9, -1):
    output += str(s[i])
print(f"\n{inp1} + {inp2} = {output}")
print(f"In decimal: {int(inp1, 2)} + {int(inp2, 2)} = {int(output, 2)}")






