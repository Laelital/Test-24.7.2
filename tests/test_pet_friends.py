from api import PetFriends
from settings import valid_email, valid_password, invalid_password, invalid_name
import os
pf = PetFriends()

def test_get_api_key_for_invalid_user(email=valid_email, password=invalid_password):
    """ Проверка что запрос api ключа возвращает статус 403 при вводе неверного пароля """
    status, result = pf.get_api_key(email, password)
    assert status == 403


def test_add_new_pet_with_invalid_age1(name='Lutic', animal_type='Papion',
                                     age='0'):
    """Проверка добавления питомца с возрастом 0"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age)
    assert status == 200

def test_add_new_pet_with_invalid_animal_type(name='Lutic', animal_type='+',
                                     age='4'):
    """Проверка добавления питомца с animal_type со спец.символом """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age)
    assert status == 200

def test_add_new_pet_with_invalid_name1(name='3', animal_type='Papion',
                                     age='4'):
    """Проверка добавления питомца с именем из числа """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age)
    assert status == 200

def test_add_new_pet_with_invalid_name2(name='+', animal_type='Papion',
                                     age='4'):
    """Проверка добавления питомца с именем из спец.символа """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age)
    assert status == 200

def test_add_new_pet_with_invalid_name3(name=invalid_name, animal_type='Papion',
    age='4'):
    """Проверка добавления питомца с длинным именем"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age)
    assert status == 200

def test_add_new_pet_with_invalid_age2(name='Lutic', animal_type='Papion',
                                     age='+'):
    """Проверка добавления питомца с возрастом из спец.символа """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age)
    assert status == 200

def test_delete_pet_in_all_pets():
    """Проверка удаления чужого питомца """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, '')

    pet_id = all_pets['pets'][1]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, all_pets = pf.get_list_of_pets(auth_key, "")

    assert status == 400
    assert pet_id in all_pets.values()

def test_set_photo_csv():
    """Проверка добавления файла в формате csv"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.post_set_photo(auth_key, pet_id, pet_photo='pets.csv')
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 400

def test_set_big_photo_():
    """Проверка добавления фото в 4к"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.post_set_photo(auth_key, pet_id, pet_photo='big_photo.png')
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200






