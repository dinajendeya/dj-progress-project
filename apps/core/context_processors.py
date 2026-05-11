from django.db.utils import OperationalError, ProgrammingError

from .models import SiteProfile


def site_meta(request):
    """Expose the site profile to all templates."""
    try:
        profile = SiteProfile.get_solo()
    except (OperationalError, ProgrammingError):
        # DB not migrated yet (e.g. during initial setup)
        profile = None
    return {"site_profile": profile}
