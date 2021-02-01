# Poke-api
## Micro-proyecto de consumo de api y estructura de información.

Esta aplicación permite mediante el nombre de un pokémon el consumo de la información relacionada con el, sus pre.evoluciones y evoluciones (en caso de tenerlas).

La información mostrada es:

- Nombre
- ID
- HP
- Ataque
- Defensa
- Ataque Especial
- Defensa Especial
- Velocidad

Inserción de información
========================
La información se obtiene de la API https://pokeapi.co/ y se almacena en la base de datos de la aplicación. El comando para la inserción es:  
    ```$ py manage.py runscript -v2 poke_insert --script-args NUMERO```  
Siendo NUMERO el digito de identificación de la cadena de evolución de los pokémones a almacenar.  

Consumo del web service
=======================
Para el consumo de la información almacenada en la aplicación, solo hay que acceder la dirección del servidor seguido del nombre del pokémon, ejemplo:  
    ```localhost:800/bulbasaur/```  
    
__La aplicación solo permite la búsqueda con el nombre de pokémon en minúscula__
