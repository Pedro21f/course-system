import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Generator


PASTA_DADOS = Path(__file__).resolve().parent
CAMINHO_BANCO = PASTA_DADOS / "materias.sqlite3"


@contextmanager
def _conectar() -> Generator[sqlite3.Connection, None, None]:
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    try:
        with conexao:
            yield conexao
    finally:
        conexao.close()

def criar_tabela() -> None:
    with _conectar() as conexao:
        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS materias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL CHECK (length(trim(nome)) > 0),
                data_criacao TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS migracoes (
                nome TEXT PRIMARY KEY
            )
            """
        )


def inserir_materia(nome: str) -> None:
    with _conectar() as conexao:
        conexao.execute("INSERT INTO materias (nome) VALUES (?)", (nome.strip(),))


def listar_materias() -> list[sqlite3.Row]:
    with _conectar() as conexao:
        return list(
            conexao.execute(
                "SELECT nome, data_criacao FROM materias ORDER BY id"
            ).fetchall()
        )


def remover_materia(nome: str) -> bool:
    with _conectar() as conexao:
        cursor = conexao.execute(
            """
            DELETE FROM materias
            WHERE id = (
                SELECT id FROM materias
                WHERE nome = ?
                ORDER BY id
                LIMIT 1
            )
            """,
            (nome,),
        )
        return cursor.rowcount > 0
