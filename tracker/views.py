from django.shortcuts import render
from .models import Transaction
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request,'index.html')


def get_transactions(request):
    data = list(Transaction.objects.values('id','text','amount'))
    return JsonResponse(data,safe=False)

@csrf_exempt
def add_transaction(request):
    if request.method == 'POST':
        try:
            print("DEBUG: Request received at add_transaction")
            
            data = json.loads(request.body)
            print(f"DEBUG: Parsed JSON data: {data}")

            text_val = data.get('text')
            amount_val = data.get('amount')


            if not text_val or not amount_val:
                print("DEBUG: Missing text or amount")
                return JsonResponse({'error': 'Missing data'}, status=400)

            print("DEBUG: Attempting to save to database...")
            transaction = Transaction.objects.create(text=text_val, amount=amount_val)
            print(f"DEBUG: Success! Saved ID: {transaction.id}")

            return JsonResponse({
                'id': transaction.id, 
                'text': transaction.text, 
                'amount': transaction.amount
            })

        except Exception as e:
            print(f"CRITICAL SERVER ERROR: {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)
            
    return JsonResponse({'error': 'Only POST requests allowed'}, status=400)

def delete_transaction(request, id):
    if request.method == "DELETE":
        transaction = Transaction.objects.get(id=id)
        transaction.delete()
        return JsonResponse({'success' : True})
    