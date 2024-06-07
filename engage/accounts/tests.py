from django.test import TestCase
from .models import *
from .admin import *
from .views import *
from .forms import *
from .apps import *


import pytest

# Create your tests here.

# Generated by CodiumAI



class TestCompanyAdmin:

    # displays company name, email, phone, and website in the admin list view
    def test_list_display_fields(self):
        company_admin = CompanyAdmin(admin.ModelAdmin)
        assert company_admin.list_display == ('name', 'email', 'phone', 'website')

    # handles companies with missing or null fields gracefully
    def test_handle_missing_or_null_fields(self):
        company_admin = CompanyAdmin(admin.ModelAdmin)
        # Simulate a company with missing fields
        company = type('Company', (object,), {'name': None, 'email': None, 'phone': None, 'website': None})
        # Check if the admin can handle the missing fields without errors
        try:
            company_admin.list_display_links(company)
            assert True
        except Exception:
            assert False


class TestEmployeeAdmin:

    # correctly displays list of employees with specified fields
    def test_list_display_fields(self):
        employee_admin = EmployeeAdmin(model=Employee, admin_site=admin.site)
        assert employee_admin.list_display == ('first_name', 'last_name', 'email', 'phone', 'department', 'title', 'contract_type')

    # handles employees with missing or null fields gracefully
    def test_handle_missing_fields(self):
        employee_admin = EmployeeAdmin(model=Employee, admin_site=admin.site)
        employee = Employee(first_name=None, last_name=None, email=None, phone=None, department=None, title=None, contract_type=None)
        try:
            employee_admin.get_list_display(employee)
            assert True
        except Exception:
            assert False


class TestAccountsConfig:

    # Correct default_auto_field is set to "django.db.models.BigAutoField"
    def test_default_auto_field_is_correct(self):
        config = AccountsConfig()
        assert config.default_auto_field == "django.db.models.BigAutoField"

    # Incorrect default_auto_field value
    def test_default_auto_field_is_incorrect(self):
        config = AccountsConfig()
        assert config.default_auto_field != "django.db.models.AutoField"


class TestCompanyRegistrationForm:

    # form saves a new user with valid data
    def test_form_saves_new_user_with_valid_data(self, mocker):
        from engage.accounts.forms import CompanyRegistrationForm
        from django.contrib.auth.models import User
        from engage.accounts.models import Company

        mocker.patch('engage.accounts.models.Company.objects.create', return_value=Company(name='TestCompany', password='password123', owner=User(username='testuser')))
    
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'password123'
        }
        form = CompanyRegistrationForm(data=form_data)
        assert form.is_valid()
        user = form.save()
        assert user.username == 'testuser'
        assert user.email == 'testuser@example.com'
        assert user.is_staff
        assert hasattr(user, 'company')
        assert user.company.name == 'testuser'

    # form submission with missing username
    def test_form_submission_with_missing_username(self):
        from engage.accounts.forms import CompanyRegistrationForm

        form_data = {
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'password123'
        }
        form = CompanyRegistrationForm(data=form_data)
        assert not form.is_valid()
        assert 'username' in form.errors


class TestSave:

    # Successfully saves a user with valid data
    def test_save_user_with_valid_data(self, mocker):
        from engage.accounts.forms import CompanyRegistrationForm
        from django.contrib.auth.models import User
        from engage.models import Company

        # Mock the Company model's create method
        mocker.patch('engage.models.Company.objects.create', return_value=Company(name='TestCompany', password='password123', owner=User(username='testuser')))

        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'password123'
        }
        form = CompanyRegistrationForm(data=form_data)
        assert form.is_valid()
        user = form.save()

        assert user.username == 'testuser'
        assert user.email == 'testuser@example.com'
        assert user.is_staff
        assert hasattr(user, 'company')
        assert user.company.name == 'testuser'

    # Saving a user with an existing username
    def test_save_user_with_existing_username(self, mocker):
        from engage.accounts.forms import CompanyRegistrationForm
        from django.contrib.auth.models import User

        # Create an existing user
        User.objects.create_user(username='existinguser', email='existinguser@example.com', password='password123')

        form_data = {
            'username': 'existinguser',
            'email': 'newemail@example.com',
            'password1': 'password123',
            'password2': 'password123'
        }
        form = CompanyRegistrationForm(data=form_data)
    
        assert not form.is_valid()
        assert 'username' in form.errors



class TestCompanySetUpForm:

    # form is valid with all fields correctly filled
    def test_form_is_valid_with_all_fields_correctly_filled(self):
        data = {
            'address': '123 Main St',
            'email': 'test@example.com',
            'phone': '123-456-7890',
            'website': 'http://example.com',
            'logo': 'path/to/logo.png'
        }
        form = CompanySetUpForm(data=data)
        assert form.is_valid()

    # form submission with missing required fields
    def test_form_submission_with_missing_required_fields(self):
        data = {
            'address': '',
            'email': '',
            'phone': '',
            'website': '',
            'logo': ''
        }
        form = CompanySetUpForm(data=data)
        assert not form.is_valid()
        assert 'address' in form.errors
        assert 'email' in form.errors
        assert 'phone' in form.errors
        assert 'website' in form.errors
        assert 'logo' in form.errors


class TestEmployeeForm:

    # Form initializes correctly with valid data
    def test_form_initializes_correctly_with_valid_data(self):
        data = {
            'number': '123',
            'title': 'Mr.',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'address': '123 Main St',
            'position': 'Developer',
            'department': 'IT',
            'contract_type': 'Full-time',
            'salary': '50000',
            'status': 'Active',
            'shift': 'Day',
            'start_date': '2023-01-01',
            'end_date': '2023-12-31',
            'profile_picture': None,
        }
        form = EmployeeForm(data=data)
        assert form.is_valid()

    # Form handles invalid company ID gracefully
    def test_form_handles_invalid_company_id_gracefully(self, mocker):
        data = {
            'company': 'invalid_id',
            'number': '123',
            'title': 'Mr.',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'address': '123 Main St',
            'position': 'Developer',
            'department': 'IT',
            'contract_type': 'Full-time',
            'salary': '50000',
            'status': 'Active',
            'shift': 'Day',
            'start_date': '2023-01-01',
            'end_date': '2023-12-31',
            'profile_picture': None,
        }
        form = EmployeeForm(data=data)
        assert not form.is_valid()

class TestCompany:

    # successfully creates a company with valid data
    def test_create_company_with_valid_data(self, mocker):
        from engage.accounts.models import Company
        from django.contrib.auth.models import User

        # Mock the User model's create method
        mocker.patch('django.contrib.auth.models.User.objects.create', return_value=User(username='example_owner'))

        user = User.objects.create(username='example_owner')
        company = Company(name='Example Company', owner=user, password='password123', address='123 Example St', email='info@example.com', phone='123-456-7890', website='http://www.example.com')
        company.save()

        assert company.name == 'Example Company'
        assert company.owner.username == 'example_owner'
        assert company.password == 'password123'
        assert company.address == '123 Example St'
        assert company.email == 'info@example.com'
        assert company.phone == '123-456-7890'
        assert company.website == 'http://www.example.com'

    # creating a company with missing required fields
    def test_create_company_with_missing_required_fields(self):
        from engage.accounts.models import Company
        from django.contrib.auth.models import User
        import pytest

        user = User.objects.create(username='example_owner')

        with pytest.raises(ValueError):
            company = Company(owner=user, password='password123', address='123 Example St', email='info@example.com', phone='123-456-7890', website='http://www.example.com')
            company.save()


class TestDepartment:

    # Creating a Department with valid data
    def test_create_department_with_valid_data(self, mocker):
        from engage.accounts.models import Company, Department
        from django.contrib.auth.models import User

        # Create a mock user
        user = User(username='testuser')
        user.save()

        # Create a mock company
        company = Company(
            name='Test Company',
            owner=user,
            password='password123',
            address='123 Test St',
            email='test@example.com',
            phone='1234567890',
            website='http://example.com',
            logo='default.jpg'
        )
        company.save()

        # Create a department with valid data
        department = Department(
            name='Research and Development',
            abbreviation='R&D',
            company=company
        )
        department.save()

        # Assertions
        assert department.name == 'Research and Development'
        assert department.abbreviation == 'R&D'
        assert department.company == company

    # Creating a Department without a name
    def test_create_department_without_name(self, mocker):
        from engage.accounts.models import Company, Department
        from django.contrib.auth.models import User
        from django.db.utils import IntegrityError

        # Create a mock user
        user = User(username='testuser')
        user.save()

        # Create a mock company
        company = Company(
            name='Test Company',
            owner=user,
            password='password123',
            address='123 Test St',
            email='test@example.com',
            phone='1234567890',
            website='http://example.com',
            logo='default.jpg'
        )
        company.save()

        # Attempt to create a department without a name
        with pytest.raises(IntegrityError):
            department = Department(
                name=None,
                abbreviation='R&D',
                company=company
            )
            department.save()

class TestTitle:

    # Creating a Title with valid name, abbreviation, and company
    def test_create_title_with_valid_data(self, mocker):
        from engage.accounts.models import Title, Company
        from django.contrib.auth.models import User

        # Create a mock user
        user = User(username='testuser')
        user.save()

        # Create a mock company
        company = Company(name='Test Company', owner=user, password='password', address='123 Test St', email='test@example.com', phone='1234567890', website='http://example.com')
        company.save()

        # Create a title with valid data
        title = Title(name='Test Title', abbreviation='TT', company=company)
        title.save()

        # Assert the title was created correctly
        assert title.name == 'Test Title'
        assert title.abbreviation == 'TT'
        assert title.company == company

    # Creating a Title with an empty name
    def test_create_title_with_empty_name(self, mocker):
        from engage.accounts.models import Title, Company
        from django.contrib.auth.models import User
        from django.core.exceptions import ValidationError

        # Create a mock user
        user = User(username='testuser')
        user.save()

        # Create a mock company
        company = Company(name='Test Company', owner=user, password='password', address='123 Test St', email='test@example.com', phone='1234567890', website='http://example.com')
        company.save()

        # Attempt to create a title with an empty name
        title = Title(name='', abbreviation='TT', company=company)
    
        # Assert that saving the title raises a ValidationError
        with pytest.raises(ValidationError):
            title.full_clean()
            title.save()

class TestContractType:

    # create a Contract_type with valid name, abbreviation, and company
    def test_create_contract_type_with_valid_data(self, mocker):
        from engage.accounts.models import Company, Contract_type
        from django.contrib.auth.models import User

        # Create a mock user
        user = User(username='testuser')
        user.save()

        # Create a mock company
        company = Company(name='Test Company', owner=user, password='password', address='123 Test St', email='test@example.com', phone='1234567890', website='http://example.com')
        company.save()

        # Create a Contract_type with valid data
        contract_type = Contract_type(name='Full-time', abbreviation='FT', company=company)
        contract_type.save()

        # Assertions
        assert contract_type.name == 'Full-time'
        assert contract_type.abbreviation == 'FT'
        assert contract_type.company == company

    # create a Contract_type with a null abbreviation
    def test_create_contract_type_with_null_abbreviation(self, mocker):
        from engage.accounts.models import Company, Contract_type
        from django.contrib.auth.models import User

        # Create a mock user
        user = User(username='testuser')
        user.save()

        # Create a mock company
        company = Company(name='Test Company', owner=user, password='password', address='123 Test St', email='test@example.com', phone='1234567890', website='http://example.com')
        company.save()

        # Create a Contract_type with null abbreviation
        contract_type = Contract_type(name='Part-time', abbreviation=None, company=company)
        contract_type.save()

        # Assertions
        assert contract_type.name == 'Part-time'
        assert contract_type.abbreviation is None
        assert contract_type.company == company

class TestEmployee:

    # create an employee with all required fields
    def test_create_employee_with_all_required_fields(self, mocker):
        company = mocker.Mock(spec=Company)
        title = mocker.Mock(spec=Title)
        position = mocker.Mock(spec=Position)
        department = mocker.Mock(spec=Department)
        contract_type = mocker.Mock(spec=Contract_type)
    
        employee = Employee.objects.create(
            number="12345",
            title=title,
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="1234567890",
            address="123 Main St",
            position=position,
            department=department,
            contract_type=contract_type,
            salary=50000.00,
            start_date="2023-01-01",
            end_date=None,
            profile_picture="profile_picture/default.jpg",
            status="Active",
            shift="Day",
            company=company
        )
    
        assert employee.number == "12345"
        assert employee.first_name == "John"
        assert employee.last_name == "Doe"
        assert employee.email == "john.doe@example.com"
        assert employee.phone == "1234567890"
        assert employee.address == "123 Main St"
        assert employee.salary == 50000.00
        assert employee.start_date == "2023-01-01"
        assert employee.end_date is None
        assert employee.profile_picture == "profile_picture/default.jpg"
        assert employee.status == "Active"
        assert employee.shift == "Day"

    # create an employee with missing optional fields
    def test_create_employee_with_missing_optional_fields(self, mocker):
        company = mocker.Mock(spec=Company)
        title = mocker.Mock(spec=Title)
        position = mocker.Mock(spec=Position)
        department = mocker.Mock(spec=Department)
        contract_type = mocker.Mock(spec=Contract_type)
    
        employee = Employee.objects.create(
            number="12345",
            title=title,
            first_name="Jane",
            last_name="Smith",
            email="jane.smith@example.com",
            phone="0987654321",
            address=None,
            position=position,
            department=department,
            contract_type=contract_type,
            salary=60000.00,
            start_date="2023-02-01",
            end_date=None,
            profile_picture="profile_picture/default.jpg",
            status="Active",
            shift="Night",
            company=company
        )
    
        assert employee.number == "12345"
        assert employee.first_name == "Jane"
        assert employee.last_name == "Smith"
        assert employee.email == "jane.smith@example.com"
        assert employee.phone == "0987654321"
        assert employee.address is None
        assert employee.salary == 60000.00
        assert employee.start_date == "2023-02-01"
        assert employee.end_date is None
        assert employee.profile_picture == "profile_picture/default.jpg"
        assert employee.status == "Active"
        assert employee.shift == "Night"

class TestTitleUpdateView:

    # Successfully updates a title with valid data
    def test_successfully_updates_title_with_valid_data(self, mocker, rf):
        from engage.accounts.views import TitleUpdateView
        from engage.accounts.models import Title
        from engage.accounts.forms import TitleForm
        from django.contrib.auth.models import User

        user = mocker.Mock(spec=User)
        user.company = mocker.Mock()
        request = rf.post('/fake-url/', data={'name': 'New Title'})
        request.user = user

        title_instance = mocker.Mock(spec=Title)
        mocker.patch.object(TitleForm, 'save', return_value=title_instance)
        view = TitleUpdateView.as_view()
        response = view(request, pk=1)

        assert response.status_code == 302
        assert title_instance.company == user.company
        assert title_instance.save.called

    # Attempt to update title with invalid data
    def test_attempt_to_update_title_with_invalid_data(self, mocker, rf):
        from engage.accounts.views import TitleUpdateView
        from engage.accounts.forms import TitleForm
        from django.contrib.auth.models import User

        user = mocker.Mock(spec=User)
        request = rf.post('/fake-url/', data={'name': ''})
        request.user = user

        form = TitleForm(data={'name': ''})
        form.is_valid = mocker.Mock(return_value=False)
        mocker.patch.object(TitleForm, 'save', return_value=form)

        view = TitleUpdateView.as_view()
        response = view(request, pk=1)

        assert response.status_code == 200
        assert 'form' in response.context_data
        assert not form.save.called

class TestAddContractType:

    # User can successfully add a new contract type with valid data
    def test_add_contract_type_with_valid_data(self, mocker, rf):
        from engage.accounts.views import add_contract_type
        from engage.accounts.models import Contract_type
        from engage.accounts.forms import ContractForm
        from django.contrib.auth.models import User

        user = mocker.Mock(spec=User)
        user.company = mocker.Mock()
        user.is_authenticated = True

        request = rf.post('/add_contract_type/', {'name': 'Test Contract'})
        request.user = user

        mocker.patch('engage.accounts.views.ContractForm', return_value=ContractForm(request.POST))
        mocker.patch('engage.accounts.views.Contract_type.objects.filter', return_value=[])
        mocker.patch('engage.accounts.views.messages.success')
    
        response = add_contract_type(request)
    
        assert response.status_code == 200
        engage.accounts.views.messages.success.assert_called_once_with(request, 'Contract type added successfully')

    # Form submission with invalid data shows error message
    def test_add_contract_type_with_invalid_data(self, mocker, rf):
        from engage.accounts.views import add_contract_type
        from engage.accounts.forms import ContractForm
        from django.contrib.auth.models import User

        user = mocker.Mock(spec=User)
        user.company = mocker.Mock()
        user.is_authenticated = True

        request = rf.post('/add_contract_type/', {'name': ''})
        request.user = user

        invalid_form = ContractForm(request.POST)
        invalid_form.is_valid = mocker.Mock(return_value=False)

        mocker.patch('engage.accounts.views.ContractForm', return_value=invalid_form)
        mocker.patch('engage.accounts.views.Contract_type.objects.filter', return_value=[])
        mocker.patch('engage.accounts.views.messages.error')
    
        response = add_contract_type(request)
    
        assert response.status_code == 200
        engage.accounts.views.messages.error.assert_called_once_with(request, 'Contract type not added')

class TestAddDept:

    # Successfully adding a department with valid data
    def test_add_department_with_valid_data(self, mocker, rf, user_factory):
        user = user_factory()
        rf.user = user
        request = rf.post('/add_dept/', {'name': 'HR'})
        request.user = user

        mocker.patch('engage.accounts.views.DepartmentForm.is_valid', return_value=True)
        mocker.patch('engage.accounts.views.DepartmentForm.save', return_value=mocker.Mock())
        mocker.patch('engage.accounts.views.messages.success')
    
        response = add_dept(request)
    
        assert response.status_code == 200
        engage.accounts.views.messages.success.assert_called_once_with(request, 'Department added successfully')

    # Submitting the form with missing required fields
    def test_add_department_with_missing_fields(self, mocker, rf, user_factory):
        user = user_factory()
        rf.user = user
        request = rf.post('/add_dept/', {})
        request.user = user

        mocker.patch('engage.accounts.views.DepartmentForm.is_valid', return_value=False)
        mocker.patch('engage.accounts.views.messages.error')
    
        response = add_dept(request)
    
        assert response.status_code == 200
        engage.accounts.views.messages.error.assert_called_once_with(request, 'Department not added')


class TestCompanySetUp:

    # renders company.html with CompanySetUpForm on GET request
    def test_renders_company_html_with_form_on_get_request(self, mocker, rf):
        from engage.accounts.views import company_set_up
        from engage.accounts.forms import CompanySetUpForm
        from django.contrib.auth.models import User

        user = mocker.Mock(spec=User)
        user.company = mocker.Mock()
        request = rf.get('/company_set_up')
        request.user = user

        mocker.patch('django.contrib.auth.decorators.login_required', lambda x: x)

        response = company_set_up(request)

        assert response.status_code == 200
        assert 'accounts/company.html' in [t.name for t in response.templates]
        assert isinstance(response.context_data['set_up_form'], CompanySetUpForm)

    # handles invalid form data and re-renders company.html with errors
    def test_handles_invalid_form_data_and_rerenders_with_errors(self, mocker, rf):
        from engage.accounts.views import company_set_up
        from engage.accounts.forms import CompanySetUpForm
        from django.contrib.auth.models import User

        user = mocker.Mock(spec=User)
        user.company = mocker.Mock()
        request = rf.post('/company_set_up', data={})
        request.user = user

        mocker.patch('django.contrib.auth.decorators.login_required', lambda x: x)
        mocker.patch.object(CompanySetUpForm, 'is_valid', return_value=False)

        response = company_set_up(request)

        assert response.status_code == 200
        assert 'accounts/company.html' in [t.name for t in response.templates]
        assert isinstance(response.context_data['set_up_form'], CompanySetUpForm)

class TestCompanyCreation:

    # Successfully creates a company with valid form data
    def test_successfully_creates_company_with_valid_form_data(self, mocker):
        from engage.accounts.views import company_creation
        from django.contrib.auth.models import User
        from django.contrib.messages.storage.fallback import FallbackStorage
        from django.test import RequestFactory

        # Mock the form to return valid data
        mock_form = mocker.patch('engage.accounts.views.CompanyRegistrationForm')
        mock_form.return_value.is_valid.return_value = True
        mock_form.return_value.save.return_value = User()

        # Create a POST request
        factory = RequestFactory()
        request = factory.post('/company_creation', data={})
        request.user = mocker.Mock()
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = company_creation(request)

        assert response.status_code == 200
        assert 'Company created!' in [msg.message for msg in messages]

    # Handles invalid form data and displays form errors
    def test_handles_invalid_form_data_and_displays_errors(self, mocker):
        from engage.accounts.views import company_creation
        from django.test import RequestFactory

        # Mock the form to return invalid data
        mock_form = mocker.patch('engage.accounts.views.CompanyRegistrationForm')
        mock_form.return_value.is_valid.return_value = False
        mock_form.return_value.errors = {'name': ['This field is required.']}

        # Create a POST request
        factory = RequestFactory()
        request = factory.post('/company_creation', data={})
        request.user = mocker.Mock()

        response = company_creation(request)

        assert response.status_code == 200
        assert 'This field is required.' in str(response.content)





