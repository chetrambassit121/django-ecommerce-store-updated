import factory
from ecommerce.apps.catalogue.models import Category, ProductType, ProductSpecification, Product
from faker import Faker

fake = Faker()

####
# Catalogue
####


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "django"
    slug = "django"


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType

    name = "book"


class ProductSpecificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSpecification

    product_type = factory.SubFactory(ProductTypeFactory)
    name = "pages"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    product_type = factory.SubFactory(ProductTypeFactory)
    category = factory.SubFactory(CategoryFactory)
    title = "product_title"
    description = fake.text()
    slug = "product_slug"
    regular_price = "9.99"
    discount_price = "4.99"
