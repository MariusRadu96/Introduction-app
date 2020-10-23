from __future__ import absolute_import
import random
import json
from celery import shared_task
from .models import Vendor, Category
from .utils import create_new_game, generate_fake_names



@shared_task
def new_game():
    ind = random.choice([True, False])
    create_new_game(ind)
    

@shared_task
def new_vendors():
    for i in range(random.randint(1,5)):
        new_vendor = generate_fake_names('vendor')
        new_vendor = json.loads(new_vendor)

        if Vendor.objects.filter(slug=new_vendor['slug']).exists():
            pass
        else:
            vendor = Vendor(**new_vendor)
            vendor.save()


@shared_task
def new_categories():
    for i in range(random.randint(1,5)):
        new_category = generate_fake_names('category')
        new_category = json.loads(new_category)

        if Category.objects.filter(slug=new_category['slug']).exists():
            pass
        else:
            category = Category(**new_category)

            category.save()
