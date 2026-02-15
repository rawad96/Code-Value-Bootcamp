from time import sleep
from functools import lru_cache


@lru_cache(maxsize=3)
def fetch_date(user_id: int) -> dict:
    print(f'Fetching data for user {user_id} ...')
    sleep(3)
    return {
        'user_id': user_id,
        'name': f'user {user_id}'
    }


if __name__ == '__main__':
    for i in range(10):
        if (i % 2) == 0:
            result = fetch_date(2)
        else:
            result = fetch_date(i)
        print(f'result is {result}')

