import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class StartGameView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Extract token from the Authorization header
        token = request.headers.get('Authorization').split(" ")[1]

        # Get player 1 data from authen_service (use authen-service container name)
        authen_url = "http://authen-service:8000/api/users/profile/"
        headers = {'Authorization': f'Bearer {token}'}
        
        try:
            response = requests.get(authen_url, headers=headers)
            response.raise_for_status()  # Will raise an exception for HTTP errors
            
            player_1_data = response.json()  # Player 1 data
            
            # Here you can get player 1's name, avatar, etc.
            player1_username = player_1_data.get('display_name', '')  # Assuming `username` exists in profile
            player_1_avatar = player_1_data.get('avatar', '')

            # At this point, you would normally search for player 2 (invite, matchmaking, etc.)
            # For now, just returning player_1's data as an example
            return Response({
                "player_1": {
                    "display_name": player1_username,
                    "avatar": player_1_avatar
                }
            }, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            # Handle any errors when making the request to authen_service
            return Response({"error": "Failed to fetch user data from authen-service"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class FriendsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve token from the request
        token = request.headers.get("Authorization")
        if not token:
            return Response({"error": "Authorization token required"}, status=401)

        # Check the token format (debugging purposes)
        if not token.startswith("Bearer "):
            return Response({"error": "Invalid token format"}, status=400)

        # Strip the 'Bearer ' prefix
        token = token.split(" ")[1]

        # Get current player's username using POST request to the game-service
        try:
            player_info = requests.post(
                "http://game-service:8001/api/game/start/",  # Use POST instead of GET
                headers={"Authorization": f"Bearer {token}"},
            )

            if player_info.status_code != 200:
                return Response({"error": f"Failed to retrieve player info: {player_info.status_code}"}, status=400)

            player_data = player_info.json()

            # Extract player username
            player_username = player_data.get("player_1", {}).get("display_name")

            if not player_username:
                return Response({"error": "Player username not found"}, status=400)

        except Exception as e:
            return Response({"error": f"Error retrieving player info: {str(e)}"}, status=400)

        # Get friends list from authen_service
        try:
            response = requests.get(
                "http://authen-service:8000/api/users/friends/",
                headers={"Authorization": f"Bearer {token}"},
            )

            if response.status_code != 200:
                return Response({"error": f"Failed to retrieve friends list: {response.status_code}"}, status=400)

            friends_data = response.json()

        except Exception as e:
            return Response({"error": f"Error retrieving friends list: {str(e)}"}, status=400)

        # Filter to get only friend info (not your own)
        friends = []
        for friend in friends_data:
            # Check the friend's name with the player username
            if friend.get("sender_name") != player_username:
                friends.append({
                    "name": friend.get("sender_name"),
                    "avatar": friend.get("sender_avatar"),
                })
            elif friend.get("receiver_name") != player_username:
                friends.append({
                    "name": friend.get("receiver_name"),
                    "avatar": friend.get("receiver_avatar"),
                })

        return Response({"friends": friends})

class CombinedMatchmakingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = request.headers.get("Authorization")

        # Call /api/game/start/
        start_response = requests.post(
            "http://localhost:8001/api/game/start/",
            headers={"Authorization": token}
        )

        if start_response.status_code != 200:
            return Response({"error": "Failed to get player info"}, status=400)

        player_data = start_response.json().get("player_1", {})

        # Call /api/game/friendslist/
        friends_response = requests.get(
            "http://localhost:8001/api/game/friendslist/",
            headers={"Authorization": token}
        )

        if friends_response.status_code != 200:
            return Response({"error": "Failed to get friends list"}, status=400)

        friends_data = friends_response.json().get("friends", [])

        return Response({
            "player": player_data,
            "friends": friends_data
        })
    
    