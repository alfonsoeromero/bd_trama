from typing import List
from .models import Obra

class Query:
    def get(self, **kwargs) -> List[Obra]:
        if not kwargs:
            return Obra.objects.get_queryset()
        else:
            pass