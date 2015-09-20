import datetime
from django.core.management.base import BaseCommand
from pypro.models import User, Contributor, Task


class Command(BaseCommand):

    def _create_users(self):
        self._users = []
        u1 = User(
            user_name="fritzgroes",
            first_name="Fritz",
            last_name="Groes",
            hours_per_week=40.0)
        u1.save()
        u2 = User(
            user_name="webi",
            first_name="Christoph",
            last_name="Weber",
            hours_per_week=40.0)
        u2.save()
        u3 = User(
            user_name="huessi",
            first_name="Huessein",
            last_name="Karasu",
            hours_per_week=30.0)
        u3.save()
        u4 = User(
            user_name="dildo",
            first_name="Dietmar",
            last_name="Lanzersdorfer",
            hours_per_week=40.0)
        u4.save()
        self._users.append(u1)
        self._users.append(u2)
        self._users.append(u3)
        self._users.append(u4)

    def _create_tasks(self):
        c = Contributor(
            user=self._users[0],
            fraction_of_contribution=0.5,
            fraction_done=0)
        c.save()
        t = Task(
            name = "new features for version 1.0",
            description = "",
            #parent_task = models.ForeignKey("self", null=True, blank=True)
            #contributors = models.ManyToManyField(Contributor, null=True, blank=True)
            contributors=c,
            creation_date = datetime.datetime.now(),
            controller = self._users[2],
            start_date = datetime.datetime(2015,9,25,10),
            end_date = datetime.datetime(2015,8,10,10),
            fraction_done=0,
            status= Task.SCHEDULED)
        t.save()

    def handle(self, *args, **options):
        self._create_users()
        self._create_tasks()