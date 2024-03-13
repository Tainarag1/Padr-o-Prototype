from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Usuario(Prototype):
    def __init__(self, id, email, senha):
        self.id = id
        self.email = email
        self.senha = senha

    def clone(self):
        return Usuario(self.id, self.email, self.senha)

class Aula(Prototype):
    def __init__(self, id, url_aula, titulo):
        self.id = id
        self.url_aula = url_aula
        self.titulo = titulo

    def clone(self):
        return Aula(self.id, self.url_aula, self.titulo)

class Plano(Prototype):
    def __init__(self, id, valor, titulo, descricao):
        self.id = id
        self.valor = valor
        self.titulo = titulo
        self.descricao = descricao

    def clone(self):
        return Plano(self.id, self.valor, self.titulo, self.descricao)

class Categoria(Prototype):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def clone(self):
        return Categoria(self.id, self.nome)

class Aula_Categoria(Prototype):
    def __init__(self, Categoria_id, Aula_id):
        self.Categoria_id = Categoria_id
        self.Aula_id = Aula_id

    def clone(self):
        return Aula_Categoria(self.Categoria_id, self.Aula_id)

class Usuario_aula(Prototype):
    def __init__(self, usuario_id, aula_id):
        self.usuario_id = usuario_id
        self.aula_id = aula_id

    def clone(self):
        return Usuario_aula(self.usuario_id, self.aula_id)

class Categoria_plano(Prototype):
    def __init__(self, plano_id, categoria_id):
        self.plano_id = plano_id
        self.categoria_id = categoria_id

    def clone(self):
        return Categoria_plano(self.plano_id, self.categoria_id)

class Usuario_plano(Prototype):
    def __init__(self, id_plano, id_usuario):
        self.id_plano = id_plano
        self.id_usuario = id_usuario

    def clone(self):
        return Usuario_plano(self.id_plano, self.id_usuario)