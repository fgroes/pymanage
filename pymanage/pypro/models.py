from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    hours_per_week = models.FloatField()

    def __unicode__(self):
        return u"User({0}: {1} {2})".format(self.user_name, self.last_name, self.first_name)


class Contributor(models.Model):
    user = models.ForeignKey(User)
    fraction_of_contribution = models.FloatField()
    fraction_done = models.FloatField()

    def __unicode__(self):
        return "Contributor({0}: {1})".format(self.user.__unicode__(), self.fraction_of_contribution)


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    parent_task = models.ForeignKey("self", null=True, blank=True)
    contributors = models.ManyToManyField(Contributor, null=True, blank=True)
    creation_date = models.DateTimeField()
    controller = models.ForeignKey(User)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    fraction_done = models.FloatField()
    CREATED = 0
    SCHEDULED = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    DONE = 4
    status = models.IntegerField(
        choices=(
            (CREATED, "created"),
            (SCHEDULED, "scheduled"),
            (IN_PROGRESS, "in progress"),
            (COMPLETED, "completed"),
            (DONE, "done"),
    ))

    def __unicode__(self):
        return "Task({0})".format(self.name)



