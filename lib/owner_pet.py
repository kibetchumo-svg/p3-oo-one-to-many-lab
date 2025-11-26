from lib.pet import Pet

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return a list of all pets owned by this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Validate input type
        if not isinstance(pet, Pet):
            raise Exception("Can only add an instance of Pet.")
        # Set the pet's owner to this owner
        pet.owner = self

    def get_sorted_pets(self):
        # Return pets sorted alphabetically by name
        return sorted(self.pets(), key=lambda pet: pet.name)
