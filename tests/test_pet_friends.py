from api import PetFriends
from settings import valid_email, valid_password, invalid_password, invalid_name
import os
pf = PetFriends()

def test_get_api_key_for_invalid_user(email=valid_email, password=invalid_password):
    """ Проверка что запрос api ключа возвращает статус 403 при вводе неверного пароля """
    status, result = pf.get_api_key(email, password)
    assert status == 403

def test_get_all_pets_with_valid_key(filter='my_pets'):
    """Проверка что запрос api возвращает статус 200
    и список питомцев, совпадающих с фильтром в формате JSON.
    Фильтр 'my_pets' - список собственных питтомцев"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_invalid_age1(name='Lutic', animal_type='Papion',
                                     age='0'):
    """Проверяем можно ли добавить питомца с возрастом 0"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age)
    assert status == 200

def test_add_new_pet_with_invalid_animal_type(name='Lutic', animal_type='+',
                                     age='4'):
    """Проверяем можно ли добавить питомца с animal_type со спец.символом """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age)
    assert status == 200

def test_add_new_pet_with_invalid_name1(name='3', animal_type='Papion',
                                     age='4'):
    """Проверяем можно ли добавить питомца с невалидным именем (число) """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age)
    assert status == 200

def test_add_new_pet_with_invalid_name2(name='+', animal_type='Papion',
                                     age='4'):
    """Проверяем можно ли добавить питомца с невалидным именем (спец.символ) """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age)
    assert status == 200

def test_add_new_pet_with_invalid_name3(name=invalid_name, animal_type='Papion',
    age='4'):
    """Проверяем можно ли добавить питомца с невалидным именем (длинное имя)"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age)
    assert status == 200

def test_add_new_pet_with_invalid_age2(name='Lutic', animal_type='Papion',
                                     age='12+3'):
    """Проверяем можно ли добавить питомца с невалидным возрастом (спец.символ) """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet(auth_key, name, animal_type, age)
    assert status == 200

def test_delete_pet_in_all_pets():
    """Проверяем что нельзя удалить чужого питомца """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, '')

    pet_id = all_pets['pets'][1]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)
    _, all_pets = pf.get_list_of_pets(auth_key, "")

    assert status == 400
    assert pet_id in all_pets.values()

def test_set_photo_csv():
    """Проверяем что нельзя добавить файл в формате csv"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.post_set_photo(auth_key, pet_id, pet_photo='pets.csv')
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 400







