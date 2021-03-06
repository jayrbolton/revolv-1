from revolv.base.models import RevolvUserProfile
from revolv.lib.mailer import send_revolv_email

from django.conf import settings
from django.core.urlresolvers import reverse
from sesame import utils


def user_reinvestment_reminder():
    """
    Mail worker

    Send email update to user that eligible for reinvestment.
    This should execute after month_allocation

    This how the script do:
    1. Read user profile with reinvest_pool >0 and subscribed_to_updates = True
    2. For each user send updated email

    """
    SITE_URL = settings.SITE_URL
    project_reinvest_list_url = SITE_URL + reverse('reinvest_list')
    project_portfolio_url = SITE_URL + reverse('dashboard')
    unsubscribe_update_url = SITE_URL + reverse('unsubscribe', kwargs={'action': 'updates'})
    for user in RevolvUserProfile.objects.filter(reinvest_pool__gt=0.0, subscribed_to_updates=True):
        data = dict()
        amount=user.reinvest_pool
        if amount > 0.00:
            data['amount'] = amount
            data['portfolio_link'] = project_portfolio_url + utils.get_query_string(user.user)
            data['projects_url'] = project_reinvest_list_url + utils.get_query_string(user.user)
            data['unsubscribe_url'] = unsubscribe_update_url + utils.get_query_string(user.user)
            if user.user.first_name:
                data['first_name'] = user.user.first_name.title()
            else:
                data['first_name'] = 'RE-volv Supporter'
            if user.repayment_notification:
                send_revolv_email(
                    'reinvestment_reminder',
                    data, [user.user.email]
                )
            