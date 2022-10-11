from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Address, Person, Account
from .serializers import ParkingSerializer, PersonalSerializer, AccountStatusSerializer


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'PostAddress': '/person-address/',
        'GetAddress': '/address-detail/',
        'PostDetail': '/post-cardetail/',
        'GetDetail': '/get-cardetail/',
        'Exit': '/car-exit/<str:pk>/',
        'PostAccountDetails': '/person-account/',
        'GetAccountDetails': '/get-accountdetail/',
        'UpdateAccountDetails': '/person-accountupdate/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['POST'])
def personAddress(request):
    serializer = ParkingSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def addressDetail(request):
    tasks = Address.objects.all().order_by('-id')
    serializer = ParkingSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postCarDetail(request):
    serializer = PersonalSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def getCarDetail(request):
    tasks = Person.objects.all().order_by('-id')
    serializer = PersonalSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def carExit(request, pk):
    task = Person.objects.get(id=pk)
    task.delete()

    return Response('Car has exited the parking lot!')


@api_view(['POST'])
def personAccount(request):
    serializer = AccountStatusSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def getAccountDetail(request):
    tasks = Account.objects.all().order_by('-id')
    serializer = AccountStatusSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def personAccountUpdate(request, pk):
    task = Account.objects.get(id=pk)
    serializer = AccountStatusSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)