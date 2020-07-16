from django.shortcuts import render


def index(request):
    return render(request, "shareRestaurants/index.html")


def restaurant_detail(request):
    return render(request, "shareRestaurants/restaurantDetail.html")


def restaurant_create(request):
    return render(request, "shareRestaurants/restaurantCreate.html")


def category_create(request):
    return render(request, "shareRestaurants/categoryCreate.html")
