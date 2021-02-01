from django.shortcuts import render
from django.http import JsonResponse
from .models import Pokemon

def json_pokemon(request, pokemon_name):
    pokemon = Pokemon.objects.get(name=pokemon_name)

    pokemones = Pokemon.objects.filter(chain_evol_id= pokemon.chain_evol_id).values()
    pokemones = list(pokemones)
    data = {'data': pokemones}

    return JsonResponse(data)