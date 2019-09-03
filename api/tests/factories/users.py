import factory
from faker import Factory as FakerFactory


faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    """User factory."""
    username = factory.LazyAttribute(lambda x: faker.name())
    email = factory.LazyAttribute(lambda x: faker.email())
    is_staff = factory.LazyAttribute(lambda x: x or False)

    class Meta:
        model = 'auth.User'
