from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import DefaultIndexDashboard, Dashboard
from jet.dashboard.modules import ModelList, AppList, RecentActions

from demo.dashboard_module import TotalOrdersWidget


class CustomDashboard(Dashboard):
    """
    Custom dashboard for the Django Jet admin interface.
    """
    columns = 3

    def init_with_context(self, context):
        """
        Initialize the dashboard with the context.
        """
        self.available_children.append(TotalOrdersWidget)
        self.available_children.append(modules.LinkList)
        self.available_children.append(AppList)
        self.available_children.append(ModelList)
        self.available_children.append(RecentActions)

        self.children.append(TotalOrdersWidget("Total Orders"))
        self.children.append(AppList("Applications"))
        self.children.append(RecentActions("Recent Actions"))
        self.children.append(ModelList("Model List"))

        self.children.append(modules.LinkList(
            _('Support'),
            children=[
                {
                    'title': _('Django documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },
                {
                    'title': _('Django "django-users" mailing list'),
                    'url': 'http://groups.google.com/group/django-users',
                    'external': True,
                },
                {
                    'title': _('Django irc channel'),
                    'url': 'irc://irc.freenode.net/django',
                    'external': True,
                },
            ],
            column=0,
            order=0
        ))
