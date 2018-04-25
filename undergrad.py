import abce
import random
from abce import NotEnoughGoods


class Undergrad(abce.Agent, abce.Trade):
    def init(self, lot, num_undergrads, initial_cost):
        self.num_agents = num_undergrads
        self.lot = lot
        if self.id % 2 == 0:
            self.create('teddies', 2)
            self.price = self.buy_price = initial_cost
        else:
            self.price = self.lot

        self.buy_price = 0
        self.create('money', 10)

        self.sale = None

    def offer_teddy(self):
        self.price = self.price * (0.5 + random.random())
        if self['teddies'] >= 1:
            id = random.randrange(0, self.num_agents)
            self.sale = self.sell(('undergrad', id),
                                  good='teddies',
                                  quantity=1,
                                  price=self.price)

    def buy_teddy(self):
        offers = self.get_offers('teddies')
        for offer in offers:
            if offer.price <= self.lot:
                try:
                    self.accept(offer)
                    self.buy_price = offer.price
                except NotEnoughGoods:
                    pass

        self.log('price', self.buy_price)

    def adjust_price(self):
        if self.sale:
            if self.sale.status == 'rejected':
                self.price = max(self.price * 0.99, self.buy_price)

