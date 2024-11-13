



class Basket():
    
    def __init__(self, request):                                                 #self- setting func that within the class other func any other attribs
        self.session = request.session
        
        basket = self.session.get('s_key')          #cheking for previous session
        if 's_key' not in request.session:
            basket = self.session['s_key'] = {}     
        self.basket = basket

    def add(self, product, qty):

        product_id = product.id

        if product_id not in self.basket:
            self.basket[[product_id]] = {'price': str(product.price), 'qty': int(qty)}

        self.session.modified = True 

        