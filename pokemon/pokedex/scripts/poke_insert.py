import json
import requests
from pokedex.models import Pokemon

def url_conexion(id):
	id = str(id)
	url = "https://pokeapi.co/api/v2/pokemon-species/" + id
	response = requests.request("GET", url)
	species_data = response.json()
	return species_data['evolution_chain']['url']

def data_chain(url):
	response = requests.request("GET", url)
	chain_data = response.json()

	elemt = []
	chain_id = chain_data['id']
	root = chain_data['chain']
	elemt.append(root['species']['name'])

	for f_level in root['evolves_to']:
		elemt.append(f_level['species']['name'])
	for s_level in f_level['evolves_to']:
		elemt.append(s_level['species']['name'])
	return {'data': elemt, 'chain_id': chain_id}

def data_pokemon(id, chain_id):
	ids = []
	data_export = {'name':None, 'height': None, 'weight': None, 'id': None,
                 'base_stats': {'hp':None, 'attack':None, 'defense':None,
                                'attack_sp':None, 'defense_sp':None, 'speed': None},
                 'chain_id':None
                 }
	url = "http://pokeapi.co/api/v2/pokemon/" + id

	response = requests.request("GET", url)
	data_base = response.json()

	poke_ball = Pokemon(id_pokemon = data_base['id'],
		name = data_base['name'],
		height = float(data_base['height']),
		weight = float(data_base['weight']),
		hp_base = int(data_base['stats'][0]['base_stat']),
		attack_base = int(data_base['stats'][1]['base_stat']),
		attack_sp_base = int(data_base['stats'][3]['base_stat']),
		defense_base = int(data_base['stats'][2]['base_stat']),
		defense_sp_base = int(data_base['stats'][4]['base_stat']),
		speed_base = int(data_base['stats'][5]['base_stat']),
		chain_evol_id = int(chain_id)
	)
	poke_ball.save()


def run(*args):
	if(len(args) == 0):
		print("Ingrese el ID del Pokemon a insertar.Ejemplo 'py manage.py runscript -v2 poke_insert --script-args 1'")
	elif(len(args) > 1):
		print("Ingrese un solo ID")
	else:
		id = args[0]
		if(Pokemon.objects.filter(id_pokemon=int(id)).exists()):
			print("La informacion del pokemon ya esta almacenada")
		else:
			conect = url_conexion(id)
			data = data_chain(conect)
			poke_lista = data['data']
			for pokemon in poke_lista:
				data_pokemon(pokemon, data['chain_id'])
