import React, { useState, useEffect } from 'react';
import axios from 'axios';

const PlayWithFriend = () => {
  const [playerInfo, setPlayerInfo] = useState(null);
  const [friends, setFriends] = useState([]);
  const [selectedFriend, setSelectedFriend] = useState(null);
  const [isFriendOnline, setIsFriendOnline] = useState(false);
  const [inviteEnabled, setInviteEnabled] = useState(false);
  const [inviteStatus, setInviteStatus] = useState('');

  // Helper to convert avatar path to full URL
  const getFullAvatarUrl = (avatar) => {
    if (!avatar) return '';
    if (avatar.startsWith('http')) return avatar;

    // Clean up path like ./media/avatars/user_2.jpg => media/avatars/user_2.jpg
    const cleanPath = avatar.replace(/^\.?\//, '');
    return `http://localhost:8000/${cleanPath}`;
  };

  // Fetch player info and friends list
  useEffect(() => {
    const fetchPlayerInfo = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('http://localhost:8000/api/game/matchmaking/', {
          headers: { Authorization: `Bearer ${token}` },
        });
        setPlayerInfo(response.data.player);
        setFriends(response.data.friends);
      } catch (error) {
        console.error('Error fetching player info:', error);
      }
    };

    fetchPlayerInfo();
  }, []);

  // Fetch friend status (online or offline)
  const checkFriendStatus = async (friendName) => {
    try {
      const token = localStorage.getItem('token');
      const response = await axios.get(`http://localhost:8000/api/users/search/?q=${friendName}`, {
        headers: { Authorization: `Bearer ${token}` },
      });

      if (response.data[0].status === 'online') {
        setIsFriendOnline(true);
        setInviteEnabled(true);
      } else {
        setIsFriendOnline(false);
        setInviteEnabled(false);
      }
    } catch (error) {
      console.error('Error fetching friend status:', error);
    }
  };

  // Send game invite to selected friend
  const sendGameInvite = async () => {
    if (!selectedFriend) return;
  
    try {
      const token = localStorage.getItem('token');
      const response = await axios.post(
        'http://localhost:8000/api/game/invite/',
        { receiver_id: selectedFriend.id },
        {
          headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
        }
      );
  
      if (response.status === 201) {
        setInviteStatus('sent');
        console.log("Game invitation sent successfully");
      }
    } catch (error) {
      console.error('Error sending game invite:', error);
      
      // Check for specific error messages
      if (error.response && error.response.data && error.response.data.error) {
        alert(`Error: ${error.response.data.error}`);
      } else {
        setInviteStatus('failed');
      }
    }
  };

  return (
    <div className="play-with-friend-container flex justify-center items-center p-10  ">
      <div className="w-full max-w-3xl bg-white rounded-lg shadow-lg p-8">
        {/* Player Info */}
        <div className="player-info flex items-center justify-between mb-8">
          {playerInfo ? (
            <div className="flex items-center">
              <img
                src={getFullAvatarUrl(playerInfo.avatar)}
                alt="Player Avatar"
                className="w-16 h-16 rounded-full mr-6"
              />
              <span className="text-3xl font-semibold text-black">
                {playerInfo.display_name}
              </span>
            </div>
          ) : (
            <p className="text-lg text-black">Loading player info...</p>
          )}
        </div>

        {/* Friends List */}
        <div className="friends-list mb-8">
          <h3 className="text-2xl font-semibold text-black mb-6">Select a Friend</h3>
          <select
            onChange={(e) => {
              const friend = friends.find((f) => f.name === e.target.value);
              setSelectedFriend(friend);
              setIsFriendOnline(false);
              setInviteEnabled(false);
              setInviteStatus('');
            }}
            className="w-full p-4 border border-gray-300 rounded-md mb-6 text-lg"
          >
            <option>Select a friend</option>
            {friends.map((friend) => (
              <option key={friend.name} value={friend.name}>
                {friend.name}
              </option>
            ))}
          </select>

          <button
            onClick={() => checkFriendStatus(selectedFriend?.name)}
            disabled={!selectedFriend}
            className="w-full p-4 bg-blue-600 text-white rounded-md mb-6 text-lg"
          >
            Check Status
          </button>
        </div>

        {/* Selected Friend Info */}
        {selectedFriend && (
          <div className="selected-friend-info flex justify-between items-center mb-8">
            <div className="flex items-center">
              <img
                src={getFullAvatarUrl(selectedFriend.avatar)}
                alt="Selected Friend Avatar"
                className="w-16 h-16 rounded-full mr-6"
              />
              <span className="text-xl text-black">{selectedFriend.name}</span>
            </div>
            <div>
              {isFriendOnline ? (
                <p className="text-green-500 text-xl">Online</p>
              ) : (
                <p className="text-red-500 text-xl">Offline</p>
              )}
            </div>
          </div>
        )}

        {/* Invite Button */}
        <div className="flex justify-center">
          <button
            onClick={sendGameInvite}
            disabled={!inviteEnabled}
            className={`w-full py-4 text-white text-xl rounded-md ${
              inviteEnabled ? 'bg-blue-600 hover:bg-blue-700' : 'bg-gray-400'
            }`}
          >
            {inviteStatus === 'sent'
              ? 'Invitation Sent'
              : inviteStatus === 'failed'
              ? 'Failed to Send Invite'
              : inviteEnabled
              ? 'Send Game Invite'
              : 'Friend is Offline'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default PlayWithFriend;
