import time

# Create your views here.
def contar_esperar(request):
    for i in range(0, 10000):
        print(i)
        time.sleep(i)