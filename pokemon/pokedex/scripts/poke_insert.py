import json
import requests

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

	data_export['name'] = data_base['name']
	data_export['height'] = data_base['height']
	data_export['weight'] = data_base['weight']
	data_export['id'] = data_base['id']
	data_export['chain_id'] = chain_id

	data_export['base_stats']["hp"] = data_base['stats'][0]['base_stat']
	data_export['base_stats']["attack"] = data_base['stats'][1]['base_stat']
	data_export['base_stats']["attack_sp"] = data_base['stats'][3]['base_stat']
	data_export['base_stats']["defense"] = data_base['stats'][2]['base_stat']
	data_export['base_stats']["defense_sp"] = data_base['stats'][4]['base_stat']
	data_export['base_stats']["speed"] = data_base['stats'][5]['base_stat']

	return data_export

