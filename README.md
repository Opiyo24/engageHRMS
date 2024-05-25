ENGAGE HUMAN RESOURCE MANAGEMENT SYSTEM

Demo link: https://link.link.com

GITHUB
Branches
    main - main branch for final source code
    dev - development branch, where all the cooking is done.


PATH
 /
    company
    register

    ########TODO
    Decorators (admin)
    Comoany update page - User relationship





class User(models.Model):
    id = models.AutoField(primary_key=True)

class Company_account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100, default='')
    password2 = models.CharField(max_length=100, default='')
    company_address = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100)
    company_phone = models.CharField(max_length=100)
    company_website = models.URLField(max_length=100)
    company_logo = models.ImageField(upload_to='company_logo', default='default.jpg')

    def __str__(self):
        return f"{self.company_name}"


Environment:


Request Method: POST
Request URL: http://localhost:8000/company/

Django Version: 4.2.13
Python Version: 3.12.3
Installed Applications:
['django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'bootstrap5',
 'accounts']
Installed Middleware:
['django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware']



Traceback (most recent call last):
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/backends/utils.py", line 89, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/backends/sqlite3/base.py", line 328, in execute
    return super().execute(query, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The above exception (NOT NULL constraint failed: accounts_company_account.user_id) was the direct cause of the following exception:
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/opiyo/Dev/engageHRMS/engage/accounts/views.py", line 36, in company_creation
    company_form.save()
    ^^^^^^^^^^^^^^^^^^^
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/forms/models.py", line 542, in save
    self.instance.save()
    ^^^^^^^^^^^^^^^^^^^^
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/models/base.py", line 814, in save
    self.save_base(
    ^
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/models/base.py", line 877, in save_base
    updated = self._save_table(
              
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/models/base.py", line 1020, in _save_table
    results = self._do_insert(
              
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/models/base.py", line 1061, in _do_insert
    return manager._insert(
           
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/models/manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/models/query.py", line 1805, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/models/sql/compiler.py", line 1822, in execute_sql
    cursor.execute(sql, params)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/backends/utils.py", line 102, in execute
    return super().execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/backends/utils.py", line 67, in execute
    return self._execute_with_wrappers(
           
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/backends/utils.py", line 80, in _execute_with_wrappers
    return executor(sql, params, many, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/backends/utils.py", line 84, in _execute
    with self.db.wrap_database_errors:
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/backends/utils.py", line 89, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/opiyo/Dev/engageHRMS/hrms/lib/python3.12/site-packages/django/db/backends/sqlite3/base.py", line 328, in execute
    return super().execute(query, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Exception Type: IntegrityError at /company/
Exception Value: NOT NULL constraint failed: accounts_company_account.user_id

