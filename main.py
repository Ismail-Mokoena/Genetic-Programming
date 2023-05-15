from product import Product

def load_products() -> list:
        products= []
        with open("products.txt", "r") as file:
            
            for line in file:
                items_list = line.rstrip().split(',')                
                products.append(Product(items_list[0],items_list[1],items_list[2]))
        file.close()
        return products


if __name__=="__main__":
    products = load_products()
    print(products)
    