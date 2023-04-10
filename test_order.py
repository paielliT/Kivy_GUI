from order import Orders

class TestPerson:
# test case for print details of Person
    def test_details(self):
        p = Orders('Supreme Nacho', '1', '12:12:10')
        print('testing details:  person')
        assert('Supreme Nacho', '1', '12:12:10') == (p.product, p.prod_num, p.order_time)



