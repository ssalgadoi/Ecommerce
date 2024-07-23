# tu_app/context_processors.py
from .models import Category

def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}
