# from django.db import models

# Create your models here.
class Tags:
    def __init__(self, name,id,created_at,updated_at):
        self.name = name
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at