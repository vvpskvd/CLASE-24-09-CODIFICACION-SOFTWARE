import pytest
from biblioteca_sistema import BibliotecaSistema
from stubs.database_stub import DatabaseStub
from stubs.auth_stub import AuthStub

def test_prestamo_exitoso():
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=1, libro_id=2)
    assert resultado == "Préstamo exitoso"
    assert (1, 2) in db_stub.prestamos_registrados

def test_usuario_no_autorizado():
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=0, libro_id=2)
    assert resultado == "Usuario no autorizado"
    assert len(db_stub.prestamos_registrados) == 0

def test_libro_no_disponible():
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=1, libro_id=3)
    assert resultado == "Libro no disponible"
    assert len(db_stub.prestamos_registrados) == 0

def test_libro_inexistente():
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado = sistema.prestar_libro(usuario_id=1, libro_id=99)
    assert resultado == "Libro no disponible"
    assert len(db_stub.prestamos_registrados) == 0

def test_varios_prestamos():
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    sistema = BibliotecaSistema(db_stub, auth_stub)

    resultado1 = sistema.prestar_libro(usuario_id=1, libro_id=1)
    resultado2 = sistema.prestar_libro(usuario_id=2, libro_id=2)
    resultado3 = sistema.prestar_libro(usuario_id=3, libro_id=3)

    assert resultado1 == "Préstamo exitoso"
    assert resultado2 == "Préstamo exitoso"
    assert resultado3 == "Libro no disponible"
    assert (1, 1) in db_stub.prestamos_registrados
    assert (2, 2) in db_stub.prestamos_registrados
    assert len(db_stub.prestamos_registrados) == 2