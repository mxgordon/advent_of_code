class Equation:
    def __init__(self, reactants: dict, products: dict, all_chemicals: dict):
        self.reactants = reactants
        self.products = products
        self.all_chemicals = all_chemicals
        self.product_name = list(products.keys())[0]

    @staticmethod
    def read(line: str, all_chemicals: dict):
        reactant_line, product = tuple(line.split(' => '))

        reactant_list = reactant_line.split(', ')
        reactant_dict = dict(map(lambda x: [x.split(' ')[1], int(x.split(' ')[0])], reactant_list))

        product = {product.split(' ')[1]: int(product.split(' ')[0])}

        return Equation(reactant_dict, product, all_chemicals)

    @staticmethod
    def find_num_fits(all_chemicals: dict, reactants: dict):
        all_nums = []

        for compound in reactants.keys():
            coeff = 1

            while all_chemicals[compound] % (coeff * reactants[compound]) != \
                    all_chemicals[compound]:

                coeff += 1

            all_nums.append(coeff - 1)
        return min(all_nums)

    @staticmethod
    def can_convert(all_chemicals: dict, reactants: dict):
        trues = []
        for chem in reactants.keys():
            trues.append(chem in all_chemicals.keys())

        return all(trues)

    def convert(self):
        if not self.can_convert(self.all_chemicals, self.reactants):
            raise ValueError("Do not have enough chemicals to fulfill the reactant requirements")

        num_conversions = self.find_num_fits(self.all_chemicals, self.reactants)

        self.all_chemicals.update({self.product_name:
                                   self.products[self.product_name] * num_conversions})

        for chemical in self.reactants.keys():
            self.all_chemicals[chemical] -= self.reactants[chemical] * num_conversions

        return self.all_chemicals

    def __repr__(self):
        return f"<Equation {self.reactants} | {self.products} | {self.all_chemicals}>"


def get_reactants_and_products(lines: list):
    reactant_line, product = zip(*map(lambda line: line.split(' => '), lines))

    reactant_list = list(map(lambda x: [x.split(' ')[1], int(x.split(' ')[0])], reactant_line))

    product_list = list(map(lambda x: [x.split(' ')[1], int(x.split(' ')[0])], product))

    print(len(reactant_list), reactant_list, '\n', len(product), product_list)

    # reactant_list = reactant_line.split(', ')
    # reactant_dict = dict(map(lambda x: [x.split(' ')[1], int(x.split(' ')[0])], reactant_list))
    #
    # product = {product.split(' ')[1]: int(product.split(' ')[0])}



with open('data.txt', 'r') as f:
    equations = list(map(lambda x: x[:-1], f.readlines()))


if __name__ == '__main__':
    get_reactants_and_products(equations)

    current_inventory = {"ORE": 1000000}

    equation_objs = list(map(lambda x: Equation.read(x, {}), equations))
    # print(*equation_objs, sep='\n')

    while True:
        print(len(equation_objs))
        print(current_inventory["ORE"])

        # if len(equation_objs) == 16:
        #     print(*equation_objs, sep='\n')

        for equ in equation_objs:

            # print("***", equation_objs.index(equ))

            # if equation_objs.index(equ) == 41:
            #     print(equation_objs.index(equ) == 41)
            equ.all_chemicals = current_inventory
            try:
                current_inventory = equ.convert()
                assert min(current_inventory.values()) >= 0
            except ValueError:
                continue

            else:
                equation_objs.pop(equation_objs.index(equ))
                break
        if len(equation_objs) == 0:
            break
    print(current_inventory)