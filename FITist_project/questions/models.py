from django.db import models


class Question(models.Model):
    """Model for all initial questions."""

    prompt = models.TextField()
    order = models.IntegerField(default=0)
    label = models.CharField(default="", max_length=255)

    class Meta(object):
        """This is a new style class inheriting from object.

        Questions will be ordered by the order they were created.
        """

        ordering = ['order', ]

    def __str__(self):
        """Will return the question prompt as the query object description."""
        return self.prompt


class Answer(models.Model):
    """Model for answers to initial questions."""

    question = models.ForeignKey(Question)
    order = models.IntegerField(default=0)
    text = models.CharField(max_length=255)

    class Meta(object):
        """This is a new style class inheriting from object.

        Answer will be ordered by number created.
        """

        ordering = ['order', ]

    def __str__(self):
        """Will return the answer text as the query object description."""
        return self.text
