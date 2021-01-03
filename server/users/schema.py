import graphene
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django_filters import FilterSet, OrderingFilter
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


class UserFilter(FilterSet):
    class Meta:
        model = get_user_model()
        fields = {
            "username": ["icontains"],
        }

    order_by = OrderingFilter(fields=(("id", "id"), ("username", "username")))


class UserNode(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "groups")
        filterset_class = UserFilter

        interfaces = (relay.Node,)


class GroupNode(DjangoObjectType):
    class Meta:
        model = Group
        fields = ("id", "name")
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    user = relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)

    group = relay.Node.Field(GroupNode)

    def resolve_users(self, info, **kwargs):
        return get_user_model().objects.prefetch_related("groups")
