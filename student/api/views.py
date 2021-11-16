from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StudentSerialzer
from .models import Student


@api_view(['GET'])
def studentsList(request):
    students = Student.objects.all().order_by('id')
    serializer = StudentSerialzer(students, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def studentDetails(request, pk):
    student = Student.objects.get(id=pk)
    serialzer = StudentSerialzer(student, many=False)
    return Response(serialzer.data)



@api_view(['POST'])
def studentAdd(request):
     serializer = StudentSerialzer(data=request.data)
     if serializer.is_valid():
          serializer.save()
          return Response({"student added succesfully" : serializer.data })
     return Response(serializer.errors)



@api_view(['PUT'])
def studentUpdate(request,pk):
     student = Student.objects.get(id=pk)
     serilizer = StudentSerialzer(instance=student,data=request.data)
     if serilizer.is_valid():
          serilizer.save()
          return Response('student updated')
     return Response(serilizer.error)

@api_view(['DELETE'])
def studentDelete(request,pk):
     student = Student.objects.get(id=pk)
     if student:
          student.delete()
          return Response('student successfully deleted')
     return Response(student.error)