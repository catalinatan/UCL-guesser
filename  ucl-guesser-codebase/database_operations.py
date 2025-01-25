from firebase_admin import db

def add_building(building_data):
    ref = db.reference('buildings')
    ref.push(building_data)

def get_buildings():
    ref = db.reference('buildings')
    return ref.get()

def update_user_points(user_id, points):
    ref = db.reference(f'users/{user_id}/points')
    ref.set(points)
