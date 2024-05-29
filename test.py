import msgspec

data = b'''{"a": 1,"b": 2,"c": 3, "system": "Windows","abuse": "valueof"}'''


class Base(msgspec.Struct):
    a: int
    b: int
    c: int

class Main(Base):
    system: str
    abuse: str


a = msgspec.json.decode(
    data,
    type=Main, 
    strict=False
)

print(a.system)