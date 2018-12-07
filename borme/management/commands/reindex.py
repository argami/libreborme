from django.core.management.base import BaseCommand
from borme.models import Company
from borme.documents import CompanyDocument, PersonDocument
from borme.documents import idx
from borme.models import Company, Person
from tqdm import tqdm


class Command(BaseCommand):
    help = 'Find a company and show its information'

    def add_arguments(self, parser):
        parser.add_argument("year", type=str, help="year to sync")

    def handle(self, *args, **options):
        year = options["year"]

        cd = CompanyDocument()
        c = tqdm(Company.objects.filter(date_updated__year=year).iterator())
        cd.update(thing=c)
        print()


