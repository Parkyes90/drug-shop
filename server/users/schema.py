import graphene
from django.contrib.auth import get_user_model
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


class UserNode(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email")
        filter_fields = {
            "username": ["icontains"],
        }
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    all_users = DjangoFilterConnectionField(UserNode)
