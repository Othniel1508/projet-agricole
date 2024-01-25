from django.shortcuts import render
from .models import Consommateur
from django.http import HttpResponseRedirect


def formulaire_consommateur(request):
    if request.method == 'POST':
        consommateur_id = request.POST['consommateur_id']
        bio = request.POST['bio'] == 'true'
        local = request.POST['local'] == 'true'
        sans_gluten = request.POST['sans_gluten'] == 'true'
        vegetarien = request.POST['vegetarien'] == 'true'
        vegetalien = request.POST['vegetalien'] == 'true'
        produit1 = request.POST['produit1']
        avis1 = request.POST['avis1']
        evaluation1 = request.POST['evaluation1']
        date_evaluation1 = request.POST['date_evaluation1']
        produit2 = request.POST['produit2']
        avis2 = request.POST['avis2']
        evaluation2 = request.POST['evaluation2']
        date_evaluation2 = request.POST['date_evaluation2']
        produit_demande1 = request.POST['produit_demande1']
        motif_demande1 = request.POST['motif_demande1']
        produit_demande2 = request.POST['produit_demande2']
        motif_demande2 = request.POST['motif_demande2']

        Consommateur.objects.using('consommateur').create(
            consommateur_id=consommateur_id,
            bio=bio,
            local=local,
            sans_gluten=sans_gluten,
            vegetarien=vegetarien,
            vegetalien=vegetalien,
            produit1=produit1,
            avis1=avis1,
            evaluation1=evaluation1,
            date_evaluation1=date_evaluation1,
            produit2=produit2,
            avis2=avis2,
            evaluation2=evaluation2,
            date_evaluation2=date_evaluation2,
            produit_demande1=produit_demande1,
            motif_demande1=motif_demande1,
            produit_demande2=produit_demande2,
            motif_demande2=motif_demande2
        )

        return HttpResponseRedirect(request.path)
    else:
        return render(request, 'consommateur.html')
