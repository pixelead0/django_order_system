import time

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """
    Tries to do and apply migrations.

    Until the database is ready to receive connections.
    """

    help = "Intenta hacer y aplicar las migraciones hasta que la "
    "base de datos esté lista para recibir conexiones."

    def handle(self, *args, **options):  # noqa: D102
        self.stdout.write("Aplicando migraciones...")
        con_db = None
        while not con_db:
            try:
                call_command("migrate")
                con_db = True
                self.stdout.write(
                    self.style.SUCCESS(
                        "Las migraciones se aplicaron correctamente!",
                    )
                )
            except OperationalError:
                self.stdout.write(
                    "La base de datos no está lista, esperando un segundo..."
                )
                time.sleep(1)
