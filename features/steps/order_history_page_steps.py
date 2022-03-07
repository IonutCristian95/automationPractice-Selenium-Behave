from behave import *


@then('orderHistoryPage: user will view current orders - one paid by bankwire and one by cheque')
def step_impl(context):
    context.order_history_page.placed_orders_payments()
