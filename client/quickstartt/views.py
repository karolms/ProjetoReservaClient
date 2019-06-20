from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from client.quickstartt.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from client.quickstartt.serializers import ReservaSerializer
from rest_framework import status
import serial 


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



def envia_dados_pro_arduino(dados_string):
    #init serial port and bound
    # bound rate on two ports must be the same
    ser = serial.Serial('/dev/ttyS2', 9600)
    print(ser.portstr)

    #send data via serial port
    ser.write(dados_string)
    ser.close()


@api_view(['POST'])
def fazer_reserva(request):
	serializer = ReservaSerializer(data=request.data)
	if serializer.is_valid():
		print(request.data)
		dados = request.data
		envia_dados_pro_arduino(dados)
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



