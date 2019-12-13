import requests

def test_get_locations_for_us_46143_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/46143")
    assert response.status_code == 200

def test_get_locations_for_us_46143_check_content_type_equals_json():
    response = requests.get("http://api.zippopotam.us/us/46143")
    assert response.headers['Content-Type'] == "application/json"

def test_get_locations_for_us_46143_check_country_equals_united_states():
    response = requests.get("http://api.zippopotam.us/us/46143")
    response_body = response.json()
    assert response_body['country'] == "United States"
    
def test_get_locations_for_us_46143_check_city_equals_greenwood():
    response = requests.get("http://api.zippopotam.us/us/46143")
    response_body = response.json()
    assert response_body['places'][0]['place name'] == "Greenwood"

def test_get_locations_for_us_46143_check_one_place_returned():
    response = requests.get("http://api.zippopotam.us/us/46143")
    response_body = response.json()
    assert len(response_body['places']) == 1
