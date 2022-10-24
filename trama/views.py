from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from trama.models import Obra
from trama.utils.buscador import Buscador


def index(request):
    return render(request, "index.html")


def administrar(request):
    return render(request, "index.html")


def search(request):
    return render(request, "search.html")


def listado(request):
    num_per_page = 10
    obras = Paginator(Obra.objects.all().order_by("id"), num_per_page)
    page_number = request.GET.get("pagina")
    if page_number is None:
        page_number = 1
    else:
        # Todo check if `page_number` is a positive integer and if not,
        # return a 404
        page_number = int(page_number)
    offset = (page_number - 1)*num_per_page
    pagina_obj = obras.get_page(page_number)
    return render(request, "listado.html",
                  {"result": pagina_obj,
                   "offset": offset})


def search_result(request):
    if request.method == "GET":
        query_text = request.GET.get("query", "")
        buscador = Buscador(query_text=query_text)
        query_results = buscador.get()
        return render(request, "search.html",
                      {"query": query_text,
                       "query_result": query_results})


def acerca(request):
    return render(request, "acerca.html")


def obra(request, obra_id):
    obra = get_object_or_404(Obra, pk=obra_id)
    return render(request, "obra.html", {"obra": obra})
