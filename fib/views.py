from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def fib(request):
    n = request.GET.get('n')
    n = int(n)
    if n <= 0:
        return JsonResponse({"status": 400, "message": 'Bad request'})
    fib_sequence = [0, 1]
    while len(fib_sequence) <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return JsonResponse({'result': fib_sequence[n]})