"""Defines the Role model/schema"""
from enum import Enum

class Role(str, Enum):
    OPERATION_MANAGER = "operation manager"
    GENERAL_MANAGER = "general manager"
    ADMIN = "admin"
    SALES_OFFICER = "sales officer"
    STOREKEEPER = "storekeeper"
    FINANCE_PERSONAL = "finance personal"
    FULFILLMENT_SUPERVISOR = "fulfillment supervisor"
    DELIVERY_AGENT = "delivery agent"


