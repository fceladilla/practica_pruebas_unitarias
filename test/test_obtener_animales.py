import allure
from animales import obtener_nombre_animales

@allure.description('Test donde se devuelve una lista de nombre de animales')
@allure.feature('Animales')
@allure.epic('Listas de nombres')

def test_obtener_nombres():
    nombres=obtener_nombre_animales()
    assert isinstance(nombres,list)
