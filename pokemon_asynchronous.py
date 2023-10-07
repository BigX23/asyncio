import random
import asyncio
import requests
import time

MAX_POKEMON = 898

async def get_random_pokemon_name_async():
    url = "https://pokeapi.co/api/v2/pokemon/"
    pokemon_id = str(random.randint(1, MAX_POKEMON))
    response = requests.get(url + pokemon_id)
    pokemon_name = response.json()["name"]
    return pokemon_name


async def main():
    pokemon_name = await get_random_pokemon_name_async()
    print(f"Pokemon name: {pokemon_name}")


if __name__ == "__main__":
    asyncio.run(main())
