# YouTube Features Testing with Selenium and Pytest

## Project Overview
This project automates the testing of YouTube's features using **Python**, **Selenium**, and **Pytest**. The tests are organized into two main categories:
1. **Features That Require Authentication**
2. **Features That Do NOT Require Authentication**

The automated tests ensure the functionality of these features, improving efficiency and accuracy in verifying their behavior.

---

## Features Tested

### Features That Require Authentication
These features are tied to user accounts and require login credentials.

#### Left Sidebar (Navigation Panel)
1. Subscriptions - Displays a list of channels you are subscribed to.
2. History - Access your watch history.
3. Playlists - View your saved playlists.
4. Your Videos - Access your uploaded videos.
5. Watch Later - Displays videos saved to watch later.
6. Liked Videos - A playlist of all videos you've liked.
7. Subscriptions List - Displays a list of subscribed channels (e.g., Bloomberg, CNN).

#### Right Sidebar (Video Context Options)
1. Save to Watch Later - Save the video to the "Watch Later" playlist.
2. Save to Playlist - Save the video to a custom playlist.
3. Not Interested - Mark the video as "Not Interested" to remove recommendations.
4. Don't Recommend Channel - Prevent further recommendations from the channel.
5. Report - Report the video for violating YouTube policies.

#### Top Navigation Bar
1. Profile Icon (Top Right) - Access account-related options such as:
   - Switch Account
   - Manage Google Account
   - Log Out
2. Notifications (Bell Icon) - View notifications for subscriptions and comments.

#### Underneath Video Player (Video Interaction Buttons)
1. Like - Like the video.
2. Dislike - Dislike the video.
3. Save - Save the video to a playlist.
4. Subscribe/Unsubscribe - Toggle subscription to the channel.

#### Settings and More (Bottom Left)
1. YouTube Studio - Dashboard for managing videos and analytics (for content creators).

#### Comments Section
1. Comment Box - Input to add a new comment.
2. Like a Comment - Like a comment below the video.
3. Reply to Comment - Add a reply to an existing comment.

---

### Features That Do NOT Require Authentication
These features are accessible to all users without requiring login credentials.

#### Left Sidebar (Navigation Panel)
1. Home - Redirects to the YouTube homepage.
2. Shorts - Opens the Shorts section for short-form videos.
3. Explore - Expand options such as:
   - Trending
   - Shopping
   - Music
   - Movies & TV
   - Live
   - Gaming
   - News
   - Sports
   - Learning
   - Fashion & Beauty
   - Podcasts
   - Playables

#### Right Sidebar (Video Context Options)
1. Add to Queue - Add the video to the queue for later playback.
2. Share - Access sharing options (copy link, social media, etc.).

#### Top Navigation Bar
1. Search Bar - Enter keywords to search for videos, playlists, or channels.
2. Search by Voice (Microphone Icon) - Use voice commands for search functionality.

#### Video Player Buttons
1. Play/Pause - Toggle video playback.
2. Progress Bar - Navigate through the video timeline.
3. Volume Control - Adjust or mute/unmute volume.
4. Captions/Subtitles - Enable or disable captions.
5. Settings Gear - Access video settings (quality, speed, subtitles, etc.).
6. Theater Mode - Expand video to a larger view without fullscreen.
7. Fullscreen - Toggle fullscreen mode.
8. Mini-Player - Shrink video to a mini-player.

#### Settings and More (Bottom Left)
1. YouTube Premium - Redirects to the YouTube Premium subscription page.
2. YouTube TV - Redirects to YouTube's TV service.
3. YouTube Music - Opens the music streaming section.
4. YouTube Kids - Opens the child-friendly version of YouTube.
5. Settings - Access account and general platform settings.
6. Report History - View a history of reported videos.
7. Help - Redirects to YouTube's Help Center.
8. Send Feedback - Opens a feedback form for reporting platform issues.

---

## Technologies Used
- **Python**: For writing the test scripts.
- **Selenium**: For automating browser interactions.
- **Pytest**: For managing and running test cases.

---

## Setup Instructions

### Prerequisites
1. Install Python 3.10 or later.
2. Install Google Chrome and the **chromedriver** compatible with your Chrome version.
3. Install the required Python libraries:
   ```bash
   pip install selenium pytest pytest-xdist

