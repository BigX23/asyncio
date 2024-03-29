import random
import asyncio
import requests
import time

MAX_POKEMON = 898

def get_random_pokemon_name_sync():
    url = "https://pokeapi.co/api/v2/pokemon/"
    pokemon_id = str(random.randint(1, MAX_POKEMON))
    response = requests.get(url + pokemon_id)
    pokemon_name = response.json()["name"]
    return pokemon_name


def main():
    time_before = time.perf_counter()
    for _ in range(20):
        pokemon_name = get_random_pokemon_name_sync()
        print(f"Pokemon name: {pokemon_name}")
    time_after = time.perf_counter() - time_before
    print(f"Time taken: {time_after:.2f} seconds")


if __name__ == "__main__":
    main()


