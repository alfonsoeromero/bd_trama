from django.db.models import Q, QuerySet
from trama.models import Obra


class Buscador:
    def __init__(self, query_text: str) -> None:
        self._query_text = query_text

    def get(self) -> QuerySet:
        query_tokens = self._query_text.lower().split()

        query_result = None
        for token in query_tokens:
            matching_obras = Obra.objects.filter(
                Q(nombre_obra__icontains=token) |
                Q(descripcion__icontains=token) |
                Q(trabajo_representado__nombre_trabajo__icontains=token)
            ).distinct()
            if query_result is None:
                query_result = matching_obras
            else:
                query_result = query_result.union(matching_obras)
        return query_result.order_by('id')

