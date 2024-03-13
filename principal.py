from tkinter import *
from classe import *
from funcoes import*

# Iniciando o sistema
sistema = Sistema()

# Criando instâncias vazias dos protótipos
prototipo_usuario = Usuario(None, None, None)
prototipo_aula = Aula(None, None, None)
prototipo_plano = Plano(None, None, None, None)
prototipo_categoria = Categoria(None, None)
prototipo_aula_categoria = Aula_Categoria(None, None)
prototipo_usuario_aula = Usuario_aula(None, None)
prototipo_categoria_plano = Categoria_plano(None, None)
prototipo_usuario_plano = Usuario_plano(None, None)


# Criando uma categoria
cat = prototipo_categoria.clone()
cat.nome = 'GEOMETRIA'
cat.id = 1
id_categoria = cat.id

# Criando as primeiras aulas
aula = prototipo_aula.clone()
aula.url_aula = 'https://www.youtube.com/watch?v=5e8Ua4RhhXg'
aula.titulo = 'Poligonos'
aula.id = 1
id_aula = aula.id
sistema.adicionar_aula_ao_curso(aula.url_aula, aula.titulo, id_categoria)

# Repetindo o processo para cadastrar outras aulas
aula = prototipo_aula.clone()
aula.url_aula = 'https://www.youtube.com/watch?v=o-srrvPTo0Y'
aula.titulo = 'Angulos e Retas'
aula.id = 2
id_aula = aula.id
sistema.adicionar_aula_ao_curso(aula.url_aula, aula.titulo, id_categoria)

# Criando um plano
plano = prototipo_plano.clone()
plano.descricao = 'Adquira uma compreensão abrangente da geometria, desde seus princípios fundamentais até suas aplicações práticas e dimensões avançadas'
plano.valor = 50
plano.titulo = 'Desafios Geometricos'
plano.id = 1
id_plano = plano.id
sistema.adicionar_plano(plano.descricao, plano.valor, plano.titulo)

# Criando outra categoria
cat = prototipo_categoria.clone()
cat.nome = 'EQUACOES'
cat.id = 2
id_categoria = cat.id
sistema.adicionar_categoria(cat)

# Criando o segundo plano
plano = prototipo_plano.clone()
plano.descricao = 'Desbrave o universo dos sistemas de equações por meio de uma abordagem educacional meticulosa, explorando desde os fundamentos até aplicações práticas'
plano.valor = 50
plano.titulo = 'Desafios de Equacoes'
plano.id = 2
id_plano = plano.id
sistema.adicionar_plano(plano.descricao, plano.valor, plano.titulo)

# Iniciando a interface
sistema.iniciar_interface()
