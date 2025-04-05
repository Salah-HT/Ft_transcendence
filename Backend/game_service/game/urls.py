from django.urls import path
from game.views import StartGameView, FriendsListView , CombinedMatchmakingView # Import the StartGameView

urlpatterns = [
    # Other URL patterns here...
    
    path('game/start/', StartGameView.as_view(), name='start-game'),  # Add your start game API to get game id and user name
    path('game/friendslist/', FriendsListView.as_view(), name='friends-list'), #list frinds
    path('game/matchmaking/', CombinedMatchmakingView.as_view(), name="matchmaking"), #player 1 and his frind list in one

]
