from django.shortcuts import redirect, render

try:
   from books_app.forms import RecipeForm
   from recipes.models import Recipe
except Exception:
   RecipeForm = None
   Recipe = None

# Create your views here.
