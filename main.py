from product import Product
from individual import Individual

def load_products():
        with open("products.txt", "r") as file:
            for line in file:
                items_list = line.rstrip().split(',')                
                yield Product(items_list[0],items_list[1],items_list[2])

        
def print_item(chromosome_list, product_list):
    for i in range(len(chromosome_list)):
        if chromosome_list[i]=="1":
            print(product_list[i])
   
        


if __name__=="__main__":
    space_list = []
    price_list = []
    product_list = []
    limit = 3
    
    for each in load_products():
        space_list.append(each.space)
        price_list.append(each.price)
        product_list.append(each.name)
    
    #first generation
    #A 
    parent_a  = Individual(space_list, price_list, limit)
    parent_a.set_chromosome()
    parent_a.fitness()
    print_item(parent_a .chromosome, product_list)
    #B
    parent_b  = Individual(space_list, price_list, limit)
    parent_b.set_chromosome()
    parent_b.fitness()
    print("\nB:")
    print_item(parent_b.chromosome, product_list)
    
    
   