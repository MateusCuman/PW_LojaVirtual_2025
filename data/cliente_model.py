from dataclasses import dataclass

@dataclass
class Cliente:
    id: int
    nome: str
    cpf: str
    email: float
    telefone: int
    senha: str

