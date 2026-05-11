from django.apps import AppConfig

class CoreConfig(AppConfig):
  default_auto_field = "django.db.models.BigAutoField"
  name = "apps.core" 
  label = "core"

  def ready(self):
    import os
    from django.db.utils import OperationalError

    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()

        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if username and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
                print("✅ Superuser created")
            else:
                print("⚠️ Superuser already exists")

    except OperationalError:
        # Happens during migrations / startup — safe to ignore
        pass
    except Exception as e:
        print("❌ Error:", e)
