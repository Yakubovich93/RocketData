from .models import Employee

from django_seed import Seed


seeder = Seed.seeder()

seeder.add_entity(Employee, 5)

inserted_pks = seeder.execute()
