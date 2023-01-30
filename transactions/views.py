from django.http import HttpResponse
from django.shortcuts import render
from .models import Transactions
import locale


def index(request):
    if request.method == "POST":

        if not dict(request.FILES):
            return HttpResponse("sem dados")

        data = dict(request.FILES)["file"][0]

        for line in data.readlines():
            decode = line.decode("utf8")
            new_transaction = Transactions()
            new_transaction.type = decode[0]
            new_transaction.date = decode[1:9]
            locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
            new_transaction.value = locale.currency(
                (int(decode[9:19]) / 100),
                grouping=True,
            )
            new_transaction.cpf = decode[19:30]
            new_transaction.card = decode[30:42]
            new_transaction.hour = decode[42:48]
            new_transaction.store_owner = decode[48:62].strip()
            new_transaction.store_name = decode[62:81][0:-1].strip()

            new_transaction.save()

        all_transactions = Transactions.objects.all()

        return render(
            request, "transactions/data.html", {"alltransactions": all_transactions}
        )

    return render(request, "transactions/index.html")
