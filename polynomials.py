from numbers import Number
class Polynomial:
    def __init__(self,coefs):
        self.coefficients=coefs

    
    def degree(self):
        return len(self.coefficients)-1

    def __str__(self):
        coefs=self.coefficients
        # (0,3,5,1)
        #[','3x',5x^2,x^3]
        terms=[]
        terms.append(str(coefs[0])) if coefs[0] else None
        if self.degree()>=1:
            terms.append(f"{'' if coefs[1]==1 else coefs[1]}x" if coefs[1] else '')
        terms+=[f"{'' if c==1 else c}x^{d}"
        for d,c in enumerate(coefs[2:],start=2) if c]
        return ' + '.join(reversed(terms)) or "0"

    def __eq__(self,other):
        return str(self)==str(other)

    def __add__(self,other):
        if isinstance(other,Polynomial):
            minLength=min(map(lambda x: len(x.coefficients),(self,other)))
            commonCoefs=tuple((a+b for a,b in zip(self.coefficients,other.coefficients)))
            return Polynomial(commonCoefs+self.coefficients[minLength:]+other.coefficients[minLength:])
        elif isinstance(other,Number):
            return Polynomial(self)+Polynomial((other,))





