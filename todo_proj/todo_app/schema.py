import graphene
from graphene_django.types import DjangoObjectType
from .models import Todo
from .serializers import ToDoSerializer  # Your DRF serializer


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo


class Query(graphene.ObjectType):
    todos = graphene.List(TodoType)

    def resolve_todos(self, info):
        queryset = Todo.objects.all()
        return queryset


class CreateTodo(graphene.Mutation):
    class Arguments:
        title = graphene.String()

    todo = graphene.Field(TodoType)

    def mutate(self, info, title):
        serializer = ToDoSerializer(data={'title': title})
        if serializer.is_valid():
            todo = serializer.save()
            return CreateTodo(todo=todo)
        return CreateTodo(todo=None)


class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)