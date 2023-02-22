from jet.dashboard.modules import DashboardModule
from core.models import Order
from django.template.loader import render_to_string


class TotalOrdersWidget(DashboardModule):
    title = 'Total Orders'

    def render(self, request=None):
        total_orders = Order.objects.filter(ordered=True).count()
        context = {
            'total_orders': total_orders,
        }
        return render_to_string('widget/total_orders.html', context)
