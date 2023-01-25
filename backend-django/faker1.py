from rentacar.models import  Customer
from faker import Faker

def run1():
    '''
        python manage.py shell
        from faker1 import run1
        run1()
        exit()
        # https://faker.readthedocs.io/en/master/
    '''

    faker = Faker()

    for i in range(1,50):
        customer = Customer(first_name=faker.first_name(),last_name=faker.last_name(), customer_id=faker.random_int(min=1, max=50, step=1) )
        customer.save()
    print('OK')





    """
def run2():
    '''
        python manage.py shell
        from faker1 import run2
        run2()
        exit()
        # https://faker.readthedocs.io/en/master/
    '''
    from products.models import Review
    faker = Faker()

    for product in Product.objects.iterator():
        reviews = [Review(review=faker.paragraph(), product=product) for _ in range(0,4)]
        Review.objects.bulk_create(reviews)


    print('OK')
    """