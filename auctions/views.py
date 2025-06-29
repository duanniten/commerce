from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

def listing(request, listing_id):
        if request.method == "POST":
            bidForm = MakeBid(request.POST)
            if request.user.is_authenticated:
                
                if bidForm.is_valid() and request.POST['bidValue'] > request.POST['actualBid']:

                    listing = AuctionListings.objects.get(id = request.POST['listing_id'])

                    bid = Bids( 
                        bidValue = request.POST['bidValue'],
                        user = request.user,
                        listing = listing
                    )
                    bid.save()
                    return HttpResponseRedirect(reverse("index")) 
                else:
                    error_message = "Bid Should be bigger than actual Bid"
                    
            else:
                error_message = "User should be login for do a bid"
                bidForm = None
            listing = AuctionListings.objects.get(id = request.POST['listing_id'])
            listing.big_bid = request.POST['actualBid']
            context = {
                        "listing" :  listing,
                        "makeBid" : bidForm,
                        "error_message" :  error_message
                        }            
            return render(request, "auctions/listing.html", context= context)

        listing = AuctionListings.objects.all()[listing_id - 1]
        bids = Bids.objects.filter(listing=listing)
        biggerBid = 0
        for bid in bids:
            if biggerBid < bid.bidValue:
                biggerBid =  bid.bidValue

        listing.big_bid = biggerBid

        if request.user.is_authenticated:
            bid = MakeBid()
        else:
            bid = ""
        context = {
           "listing" :  listing,
            "makeBid" : bid
        }

        return render(request,"auctions/listing.html", context=context)
        
    

@login_required
def create_listing(request):
    if request.method == "POST":
        form = CreateListinigForm(request.POST)
        if form.is_valid():
            print('teste2')
            title = request.POST["title"]
            description = request.POST["description"]
            initialBid = request.POST["initialBid"]
            imageUrl = request.POST['imageUrl']
            listing = AuctionListings(
                title = title,
                description = description,
                imageUrl = imageUrl,
            )
            listing.save()
            category = request.POST['category'] 
            if category != "":       
                category = Category.objects.get(pk = category)
                listing.category.set([category])
            
            bid = Bids(
                bidValue = initialBid,
                user = request.user,
                listing = listing
            )
            bid.save()
            return HttpResponseRedirect(reverse("index")) 
        else:
            print(form.errors)
            context ={
                'form' : form
            }
            return(request, "auctions/createListing.html", context)
            
    else:
        context ={
            'form' : CreateListinigForm(),
        }
        return render(request, "auctions/createListing.html", context)

def index(request):
    listings = AuctionListings.objects.all()
    bids = Bids.objects.all()
    biggerBids = {}
    for bid in bids:
        if bid.listing in biggerBids:
            if biggerBids[bid.listing] < bid.bidValue:
                biggerBids[bid.listing] = bid.bidValue
        else:
            biggerBids[bid.listing] = bid.bidValue
    for listing in listings:
        listing.bid_value = biggerBids.get(listing, 0)

    context = {
        "listings" : listings,
    }

    return render(request, "auctions/index.html", context=context)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html", {
            "form": CreateListinigForm()
        })
