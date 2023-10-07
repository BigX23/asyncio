# import random
# import asyncio
# import requests
# import aiohttp
# import time
# import http

# MAX_POKEMON = 898

# async def get_random_pokemon_name_async():
#     url = "https://pokeapi.co/api/v2/pokemon/"
#     pokemon_id = str(random.randint(1, MAX_POKEMON))
#     response = await requests.get(url + pokemon_id)
#     pokemon_name = response.json()["name"]
#     return pokemon_name


# async def main():
#     # for _ in range(20):
#     #     pokemon_name = await get_random_pokemon_name_async()
#     #     print(f"Pokemon name: {pokemon_name}")

#     result = await asyncio.gather(*[get_random_pokemon_name_async() for _ in range(20)])
#     print(result)

# if __name__ == "__main__":
#     asyncio.run(main())



import random
import asyncio
import aiohttp
import time
import http
import random
from req_http import http_get_async

MAX_POKEMON = 898

async def get_random_pokemon_name_async():
    url = "https://pokeapi.co/api/v2/pokemon/"
    pokemon_id = str(random.randint(1, MAX_POKEMON))
    async with aiohttp.ClientSession() as session:
        async with session.get(url + pokemon_id) as response:
            pokemon_name = (await response.json())["name"]
            return pokemon_name
        
# async def get_random_pokemon_name_async() -> str:
#     pokemon_id = random.randint(1, MAX_POKEMON)
#     pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
#     pokemon = await http_get_async(pokemon_url)
#     return str(pokemon["name"])



# async def main(how_many=20):
#     time_before = time.perf_counter()
#     # for _ in range(20):
#     #     pokemon_name = await get_random_pokemon_name_async()
#     #     print(f"Pokemon name: {pokemon_name}")

#     result = await asyncio.gather(*[get_random_pokemon_name_async() for _ in range(how_many)])
#     for pokemon_name in result:
#         print(f"Pokemon name: {pokemon_name}")

#     time_after = time.perf_counter() - time_before
#     print(f"Time taken: {time_after:.2f} seconds")


async def main() -> None:
    time_before = time.perf_counter()
    result = await asyncio.gather(*[get_random_pokemon_name_async() for _ in range(20)])
    print(result)
    # for pokemon_name in result:
    #     print(f"Pokemon name: {pokemon_name}")
    time_after = time.perf_counter() - time_before
    print(f"Time taken: {time_after:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
