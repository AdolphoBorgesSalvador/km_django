from django.urls import path
from galeria.views import index
from .views import index, outra_pagina

urlpatterns = [
        path('', index),
        path('outra_pagina/', outra_pagina, name='outra_pagina'),  # Adicione a nova rota

]
