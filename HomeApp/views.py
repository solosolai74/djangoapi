# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .serlializers import EmployeeSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import permissions

class EmployeeView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List single or All
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        rec_id = kwargs.get('id')
        if rec_id:
            emp = Employee.objects.filter(id=rec_id)
            if len(emp) == 0:
                return Response({"status":"Employee record not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Employee with data
        '''
        data = {
            'firstname': request.data.get('firstname'),
            'lastname': request.data.get('lastname'),
            'age': request.data.get('age'),
            'birth_date': request.data.get('birth_date'),
            'address': request.data.get('address'),
            'designation': request.data.get('designation'),
            'rec_created_by': request.data.get('rec_created_by'),
        }

        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 4. Update
    def put(self, request, id):
        '''
        Updates the todo item with given todo_id if exists
        '''
        try:
            emp = Employee.objects.get(id=id)
        except Exception:
            return Response(
                {"res": "Employee Deos not Exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
                'firstname': request.data.get('firstname'),
                'lastname': request.data.get('lastname'),
                'age': request.data.get('age'),
                'birth_date': request.data.get('birth_date'),
                'address': request.data.get('address'),
                'designation': request.data.get('designation'),
                'rec_created_by': request.data.get('rec_created_by'),
            }

        serializer = EmployeeSerializer(instance=emp, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, id):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        try:
            emp = Employee.objects.get(id=id)
        except Exception:
            return Response(
                {"res": "Employee Deos not Exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        emp.delete()
        return Response(
            {"res": f"Employee of {emp.firstname} details or deleted"},
            status=status.HTTP_200_OK
        )
