from django.shortcuts import render
from django.views import View
from .models import TopTips


class TopTipsView(View):
    def get(self, request):
        tips = TopTips.objects.all()  # Query the database for all tips
        # Pass the tips to the template
        return render(request, 'top_tips/tips.html', {'tips': tips})