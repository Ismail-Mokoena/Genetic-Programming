from product import Product
from individual import Individual

def load_products():
        with open("products.txt", "r") as file:
            for line in file:
                items_list = line.rstrip().split(',')                
                yield Product(items_list[0],items_list[1],items_list[2])
        
def individuals()-> Individual:
    space_list = []
    price_list = []
    limit = 3
    for each in load_products():
        space_list.append(each.space)
        price_list.append(each.price)
    x = Individual(space_list, price_list, limit)
    x.set_chromosome()
    return x
        

if __name__=="__main__":
    
    i1 = individuals()
    print("Spaced", i1.space)
    print("chromosome", i1.chromosome)
    
    
    #print(load_products())
    
    
   