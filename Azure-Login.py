import os
from azure.identity import InteractiveBrowserCredential
from azure.mgmt.resource import SubscriptionClient
credential = InteractiveBrowserCredential()
subscription_client = SubscriptionClient(credential)
subscription_list = subscription_client.subscriptions.list()
for subscription in subscription_list:
print(subscription.subscription_id)
