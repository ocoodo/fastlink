from hashids import Hashids


hashids = Hashids(salt="secret", min_length=6)

def generate_short_code(id: int):
    return hashids.encode(id)
