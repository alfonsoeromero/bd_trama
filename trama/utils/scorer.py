from typing import List, Tuple

from django.db.models import QuerySet
from thefuzz import fuzz
from trama.models import Obra


class Scorer:
    def score(self, query_result: QuerySet, text: str) ->\
            List[Tuple[Obra, float]]:
        scoring_fun = fuzz.token_set_ratio
        obras: List[Obra] = query_result.all()

        scored_obras = {}
        for obra in obras:
            trabajos = [
                x.nombre_trabajo for x in
                obra.trabajo_representado.all()]
            score = max(
                scoring_fun(obra.nombre_obra, text),
                scoring_fun(obra.descripcion, text),
                scoring_fun(obra.estilo.nombre_estilo, text),
            )

            score_trabajos = max([scoring_fun(x, text)
                                  for x in trabajos])

            scored_obras[obra] = max(score, score_trabajos)
        return [(x, y) for (x, y) in
                sorted(scored_obras.items(), key=lambda x: x[1],
                       reverse=True)]
