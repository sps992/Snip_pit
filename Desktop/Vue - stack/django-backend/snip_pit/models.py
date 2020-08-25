from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    """Model to build simple snippet details"""
    team_member = (
        ("Ian Malcolm", "Ian Malcolm"),
        ("John Hammond", "John Hammond"),
        ("Alan Grant", "Alan Grant"),
        ("Dennis Nedry", "Dennis Nedry"),
        ("Dr Henry Wu", "Dr Henry Wu"),
        ("Ray Arnold", "Ray Arnold"),
    )

    created_by = models.CharField(choices=team_member, default=' ', max_length=254, blank=True, null=True)
    title = models.CharField(max_length=254, default=' ')
    description = models.TextField(default='')
    code_snippet = models.TextField(default='')
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
