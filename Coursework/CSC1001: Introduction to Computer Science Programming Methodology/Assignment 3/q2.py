# Question 2 Polynomial Derivative
# Please DO NOT modify the given function except the TODO part
# You may have your own functions if necessary

class Polynomial:
    def __init__(self, polynomial_str):
        """
        Initialize the polynomial from a string representation.
        :param polynomial_str: A string representing the polynomial (e.g., "2x^3+3x^2+5x+1")
        """
        self.polynomial = polynomial_str

    def parse_terms(self):
        """
        Parse the polynomial string into individual terms.
        :return: A list of tuples containing (coefficient, variable, exponent)
        """
        # TODO: Implement polynomial parsing

        x = "x"
        res = []
        expre = self.polynomial
        for symbol in self.polynomial:
            if not symbol.isdigit() and symbol != "+" and symbol != "^" and symbol != "-":
                x = symbol
        if self.polynomial.startswith("-"):
            expre = "-" + self.polynomial
        else:
            expre = "+" + self.polynomial
        term = []
        for i in range(len(expre)):
            if expre[i] == "+" or expre[i] == "-":
                if i > 0:
                    k = i - 1
                    while expre[k-1] != "+" and expre[k-1] != "-":
                        if k > 0:
                            k = k - 1
                        else:
                            break
                    term.append(expre[k-1: i])
        for m in range(len(expre)-1, 0, -1):
            if expre[m] == "+" or expre[m] == "-":
                term.append(expre[m: ])
                break
        if self.polynomial.startswith("-"):
            term.remove('')
        for read in term:
            for mark in range(len(read)):
                if read[mark] == "^":
                    degree = read[mark+1: ]
                    coeffi = read[: mark-1]
                    if coeffi == '+':
                        coeffi = '+1'
                    if coeffi == '-':
                        coeffi = '-1'
                    res.append((coeffi, x, degree))
            if x not in read:
                res.append((read, x, '0'))
            elif '^' not in read:
                res.append((read[: -1], x, '1'))
        return res

    def derive_term(self, coefficient, variable, exponent):
        """
        Calculate the derivative of a single term.
        :param coefficient: The coefficient of the term
        :param variable: The variable (e.g., 'x')
        :param exponent: The exponent of the term
        :return: A string representing the derivative of the term
        """
        # TODO: Implement single term derivative

        if coefficient.startswith('-'):
            coef = int(coefficient)
            expo = int(exponent)
            co = coef * expo
            if expo > 2:
                ex = expo - 1
                resu = str(co) + variable + '^' + str(ex)
            elif expo == 2:
                resu = str(co) + variable
            elif expo == 1:
                resu = str(co)
            else:
                resu = ''
            return resu
        if coefficient.startswith('+'):
            coefs = coefficient[1: ]
            coef = int(coefs)
            expo = int(exponent)
            co = coef * expo
            if expo > 2:
                ex = expo - 1
                resu = '+' + str(co) + variable + '^' + str(ex)
            elif expo == 2:
                resu = '+' + str(co) + variable
            elif expo == 1:
                resu = '+' + str(co)
            else:
                resu = ''
            return resu

    def derivative(self):
        """
        Calculate the first derivative of the polynomial.
        :return: A string representing the derivative of the polynomial
        """
        # TODO: Implement polynomial derivative calculation

        resul = ''
        for term in self.parse_terms():
            resul = resul + self.derive_term(term[0], term[1], term[2])
        if resul.startswith('+'):
            return resul[1: ]
        if resul.startswith('-'):
            return resul

# Example usage
if __name__ == '__main__':
    # Test cases
    poly1 = Polynomial("2x^3+3x^2+5x+1")
    print("Original polynomial:", poly1.polynomial)
    print("Derivative:", poly1.derivative())  # Should output: "6x^2+6x+5"

    poly2 = Polynomial("y^4-2y^2+3y-7")
    print("Original polynomial:", poly2.polynomial)
    print("Derivative:", poly2.derivative())  # Should output: "4y^3-4y+3"