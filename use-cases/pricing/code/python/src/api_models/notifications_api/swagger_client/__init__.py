# coding: utf-8

# flake8: noqa

"""
    Selling Partner API for Notifications

    The Selling Partner API for Notifications lets you subscribe to notifications that are relevant to a selling partner's business. Using this API you can create a destination to receive notifications, subscribe to notifications, delete notification subscriptions, and more.  For more information, see the [Notifications Use Case Guide](doc:notifications-api-v1-use-case-guide).  # noqa: E501

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from src.api_models.notifications_api.swagger_client.api.notifications_api import NotificationsApi

# import ApiClient
from src.api_models.notifications_api.swagger_client.api_client import ApiClient
from src.api_models.notifications_api.swagger_client.configuration import Configuration

# import models into sdk package
from src.api_models.notifications_api.swagger_client.models.aggregation_filter import AggregationFilter
from src.api_models.notifications_api.swagger_client.models.aggregation_settings import AggregationSettings
from src.api_models.notifications_api.swagger_client.models.aggregation_time_period import AggregationTimePeriod
from src.api_models.notifications_api.swagger_client.models.create_destination_request import CreateDestinationRequest
from src.api_models.notifications_api.swagger_client.models.create_destination_response import CreateDestinationResponse
from src.api_models.notifications_api.swagger_client.models.create_subscription_request import CreateSubscriptionRequest
from src.api_models.notifications_api.swagger_client.models.create_subscription_response import CreateSubscriptionResponse
from src.api_models.notifications_api.swagger_client.models.delete_destination_response import DeleteDestinationResponse
from src.api_models.notifications_api.swagger_client.models.delete_subscription_by_id_response import DeleteSubscriptionByIdResponse
from src.api_models.notifications_api.swagger_client.models.destination import Destination
from src.api_models.notifications_api.swagger_client.models.destination_list import DestinationList
from src.api_models.notifications_api.swagger_client.models.destination_resource import DestinationResource
from src.api_models.notifications_api.swagger_client.models.destination_resource_specification import DestinationResourceSpecification
from src.api_models.notifications_api.swagger_client.models.error import Error
from src.api_models.notifications_api.swagger_client.models.error_list import ErrorList
from src.api_models.notifications_api.swagger_client.models.event_bridge_resource import EventBridgeResource
from src.api_models.notifications_api.swagger_client.models.event_bridge_resource_specification import EventBridgeResourceSpecification
from src.api_models.notifications_api.swagger_client.models.event_filter import EventFilter
from src.api_models.notifications_api.swagger_client.models.get_destination_response import GetDestinationResponse
from src.api_models.notifications_api.swagger_client.models.get_destinations_response import GetDestinationsResponse
from src.api_models.notifications_api.swagger_client.models.get_subscription_by_id_response import GetSubscriptionByIdResponse
from src.api_models.notifications_api.swagger_client.models.get_subscription_response import GetSubscriptionResponse
from src.api_models.notifications_api.swagger_client.models.marketplace_filter import MarketplaceFilter
from src.api_models.notifications_api.swagger_client.models.marketplace_ids import MarketplaceIds
from src.api_models.notifications_api.swagger_client.models.order_change_type_enum import OrderChangeTypeEnum
from src.api_models.notifications_api.swagger_client.models.order_change_type_filter import OrderChangeTypeFilter
from src.api_models.notifications_api.swagger_client.models.order_change_types import OrderChangeTypes
from src.api_models.notifications_api.swagger_client.models.processing_directive import ProcessingDirective
from src.api_models.notifications_api.swagger_client.models.sqs_resource import SqsResource
from src.api_models.notifications_api.swagger_client.models.subscription import Subscription
