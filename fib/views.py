from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

# フィボナッチ数列を返す関数
def fib(n):
    n1 = 0
    n2 = 1
    for i in range(n):
        n1, n2 = n2, n1 + n2
    return n1

def fib_api(request):
    n = request.GET.get('n')
    try:
        n = int(n)
        if n <= 0:
            return JsonResponse({"status": 400, "message": 'Invalid input. Please provide a positive integer.'}, status=400)
        fib_result = fib(n)
        return JsonResponse({'result': fib_result}, status=200)
    except ValueError:
        return JsonResponse({"status": 400, "message": 'Invalid input. Please provide a valid positive integer.'}, status=400)
    except Exception as e:
        return JsonResponse({"status": 400, "message": f'Bad request: {str(e)}'}, status=400)