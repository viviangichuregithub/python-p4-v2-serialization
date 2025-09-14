#!/usr/bin/env python3
# server/seed.py

from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():
    # Initialize Faker for generating random names
    fake = Faker()

    # Clear existing data in the "pets" table
    Pet.query.delete()

    # List of possible species
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Generate 10 random pets
    pets = []
    for _ in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    # Add all pets to the database session
    db.session.add_all(pets)

    # Commit the transaction to save changes
    db.session.commit()

    print("Seeded 10 random pets successfully!")
