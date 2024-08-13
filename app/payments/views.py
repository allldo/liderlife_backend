from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests
import json
import base64
import uuid

from backend import settings

PAYMENT_GATEWAY_URL = "https://api.yookassa.ru/v3/payments"

# FYI: input data example
# data_smeni : "1 смена, 01 января-01 января, 3000 рублей."
# email : "redzumi.tao@gmail.com"
# name : "Evgenii"
# phone : "+1 (23"
# price : 123
# programm_info : "Лидер Выходного Дня"
# surname : "Bykovskikh"


@csrf_exempt
def payment_create_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            description = f"{data.get('email', '')} {data.get('programm_info', '')} {data.get('data_smeni', '')}"
            receipt = {
                "customer": {"email": data.get("email", "")},
                "items": [
                    {
                        "description": f"{data.get('programm_info', '')} {data.get('data_smeni', '')}",
                        "quantity": 1.000,
                        "amount": {"value": data.get("price", 0), "currency": "RUB"},
                        "vat_code": 1,
                        "payment_mode": "full_prepayment",
                        "payment_subject": "commodity",
                    }
                ],
            }
            payment_data = {
                "amount": {"value": data.get("price", 0), "currency": "RUB"},
                "confirmation": {"type": "embedded"},
                "metadata": data,
                "capture": "true",
                "description": description,
                "receipt": receipt,
            }

            credentials = f"{settings.YOOKASSA_ID}:{settings.YOOKASSA_KEY}"
            encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode(
                "utf-8"
            )

            idempotence_key = str(uuid.uuid4())

            headers = {
                "Authorization": f"Basic {encoded_credentials}",
                "Content-Type": "application/json",
                "Idempotence-Key": idempotence_key,
            }

            response = requests.post(
                PAYMENT_GATEWAY_URL, headers=headers, json=payment_data
            )

            if response.status_code == 200:
                confirmation = response.json().get("confirmation")
                if confirmation:
                    return JsonResponse(
                        {"status": "success", "confirmation": confirmation}
                    )
                else:
                    return JsonResponse(
                        {
                            "status": "error",
                            "message": "Confirmation not found in response",
                        },
                        status=400,
                    )
            else:
                return JsonResponse(
                    {"status": "error", "message": f"{response.text}"},
                    status=response.status_code,
                )

        except json.JSONDecodeError:
            return JsonResponse(
                {"status": "error", "message": "Invalid JSON"}, status=400
            )
        except requests.RequestException as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    else:
        return JsonResponse(
            {"status": "error", "message": "Only POST requests are allowed"}, status=405
        )
