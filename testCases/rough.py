import random
import string


def random_generator(size=8, chars=string.ascii_lowercase+string.digits):
    print(''.join(random.choice(chars) for x in range(size)))


random_generator()