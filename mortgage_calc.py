
class Mortgage():
    
    def __init__(self, sum, years, irate):
        self.sum = sum
        self.years = years
        self.irate = irate

    def calculate(self):
        monthly = self.sum*(self.irate/100/12)*(((1 + (self.irate/100/12))**(self.years*12))/((1 + (self.irate/100/12))**(self.years*12)-1))
        print("You will need to pay {:.2f} monthly for {} years!".format(monthly, self.years))

def ask_info():
    sum = int(input("Enter the mortgage amount: "))
    years = int(input("Enter the number of years: "))
    irate = float(input("Enter the interest rate: "))
    return (sum, years, irate)

def main():
    sum, years, irate = ask_info()
    mortgage = Mortgage(sum, years, irate)
    mortgage.calculate()


if __name__ == "__main__":
    main()

