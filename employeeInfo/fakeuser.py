from faker import Faker
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage
import os

User = get_user_model()
fake = Faker()

def generate_fake_users(num_users):
    for _ in range(num_users):
        user = User(
            username=fake.user_name() + '@mblbd.com',
            EmployeeName=fake.name(),
            EmployeeDesignation=fake.job(),
            EmpFunctionalDesignation='others',
            Placeofposting=fake.city(),
            EmployeeID=str(fake.unique.random_number(digits=11)),
        )
        # Generating signature and pi images
        signature_content = fake.image()
        pi_content = fake.image()
        signature_filename = f"{user.EmployeeID}_signature.jpg"
        pi_filename = f"{user.EmployeeID}_pi.jpg"
        signature_file = SimpleUploadedFile(signature_filename, signature_content, content_type='image/jpeg')
        pi_file = SimpleUploadedFile(pi_filename, pi_content, content_type='image/jpeg')
        user.signature.save(signature_filename, signature_file, save=False)
        user.pi.save(pi_filename, pi_file, save=False)
        user.save()

# Example usage to generate 5 fake users

# Example usage to generate 5 fake users
