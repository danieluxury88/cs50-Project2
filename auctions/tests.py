# Create your tests here.

from .utils import *


def main():
    print("main test")
    auction = get_all_listings().first()
    user = User.objects.all().first()
    user2 = User.objects.all().last()
    print("all Listings\n", get_all_listings())
    print("all closed Listings\n", get_all_closed_listings())
    print("all bids\n", get_all_bids())
    print("all bids of first auction\n", get_all_auction_bids(auction))
    print("all highest bid of auction\n", get_highest_auction_bid(auction))
    print("all highest bid of auction\n", get_auction_winner(auction))
    print("all auctions  \n", get_all_highest_bids())
    print("all auctions won by \n", user, get_all_auctions_won_by_user(user))
    print("all auctions won by \n", user2, get_all_auctions_won_by_user(user2))


if __name__ == "__main__":
    main()
