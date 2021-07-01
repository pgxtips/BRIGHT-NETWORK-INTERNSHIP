"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    #global variables
                        #playing video, play status (paused = 0, playing = 1)
    currently_playing = []
                #this is used as a 2d array, the structure is the playlist name followed by songs in the playlist eg. [[playlist_name1,video1, video2][playlist_name2, video1, video2]]
    playlists = []
    paused = False

    def __init__(self):
        self._video_library = VideoLibrary()


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")
        return num_videos

    def show_all_videos(self):
        """Returns all videos."""
        videos_info = self._video_library.get_all_videos()
        for i in range(0, len(self._video_library.get_all_videos())):
            print(videos_info[i].title + " (" + videos_info[i].video_id + ") ", videos_info[i].tags)

    def play_video(self, video_id):
        try:
            if not self.currently_playing:
                self.currently_playing.append(self._video_library.get_video(video_id))
                self.currently_playing.append(1)
            else:
                print("Stopping video:", self.currently_playing[0].title)
                self.currently_playing.clear()
                self.currently_playing.append(self._video_library.get_video(video_id))
                self.currently_playing.append(1)

            print("Playing video:", self.currently_playing[0].title)
        except:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if not self.currently_playing:
            print("")
        else:
            print("Stopping Video:", self.currently_playing[0].title)
            self.currently_playing.clear()

    def play_random_video(self):
        """Plays a random video from the video library."""
        num_videos = len(self._video_library.get_all_videos())

        if num_videos == 0:
            print("No videos available")
            return

        if len(self.currently_playing) > 0:
            print("Stopping video:", self.currently_playing[0].title)
            self.currently_playing.clear()

        rng = random.randint(0, num_videos-1)
        self.currently_playing.append(self._video_library.get_all_videos()[rng])
        self.currently_playing.append(1)
        print("Playing Video:", self.currently_playing[0].title)

    def pause_video(self):
        if not self.currently_playing:
            print("Cannot pause video: No video is currently playing")
            return
        elif self.currently_playing[1] == 1:
            self.currently_playing[1] = 0
            print("Pausing video:", self.currently_playing[0].title)
        else:
            print("Video already paused", self.currently_playing[0].title)

    def continue_video(self):
        if not self.currently_playing:
            print("Cannot continue video: No video is currently playing")
            return
        elif self.currently_playing[1] == 0:
            self.currently_playing[1] = 1
            print("Continuing video:", self.currently_playing[0].title)
        else:
            print("Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        if not self.currently_playing:
            print("No video is currently playing")
            return
        if self.currently_playing:
            if self.currently_playing[1] == 1:
                print("Currently playing:", self.currently_playing[0].title + " (" + self.currently_playing[0].video_id + ") ", self.currently_playing[0].tags)
            else:
                print("Currently playing:", self.currently_playing[0].title + " (" + self.currently_playing[0].video_id + ") ", self.currently_playing[0].tags, "- PAUSED")

    def create_playlist(self, playlist_name):
        name_exists = False
        video_exists = False
        for i in range(0, len(self.playlists)):
            if self.playlists[i][0].lower() == playlist_name.lower():
                name_exists = True

        if not name_exists:
            temp_playlist = [playlist_name]
            self.playlists.append(temp_playlist)
            playlist_pos = len(self.playlists)-1
            print("Successfully created new playlist:", self.playlists[playlist_pos][0])
            print(self.playlists)
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        playlist_pos = -1
        for i in range(0, len(self.playlists)):
            if self.playlists[i][0].lower() == playlist_name.lower():
                playlist_pos = i

        if playlist_pos == -1:
            print("Cannot add video to", playlist_name + ": Playlist does not exist")
            return

        if self._video_library.get_video(video_id) is None:
            print("Cannot add video to", playlist_name+": Video does not exist")
            return

        for i in range(0, len(self.playlists[playlist_pos])):
            if video_id == self.playlists[playlist_pos][i]:
                print("Cannot add video to", playlist_name+": Video already added")
                return

        self.playlists[playlist_pos].append(video_id)
        print("Added video to", playlist_name + ": " + self._video_library.get_video(video_id).title)

    def show_all_playlists(self):
        if not self.playlists:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for i in range(0, len(self.playlists)):
                print("     " + self.playlists[i][0])

    def show_playlist(self, playlist_name):
        playlist_pos = -1
        nameExist = False
        for x in range(0, len(self.playlists)):
            if self.playlists[x][0].lower() == playlist_name.lower():
                playlist_pos = x
                nameExist = True

        if not nameExist:
            print("Cannot show playlist", playlist_name+": Playlist does not exist")
            return

        if len(self.playlists[playlist_pos]) == 1:
            print("No videos here yet")
        else:
            for n in range(1, len(self.playlists[playlist_pos])):
                video_obj = self._video_library.get_video(self.playlists[playlist_pos][n])
                print(video_obj.title, video_obj.video_id, video_obj.tags)



    def remove_from_playlist(self, playlist_name, video_id):
        playlist_pos = -1
        nameExist = False
        for i in range(0, len(self.playlists)):
            if self.playlists[i][0].lower() == playlist_name.lower():
                playlist_pos = i
                nameExist = True

        if not nameExist:
            print("Cannot remove video from", playlist_name+": Playlist does not exist")
            return

        if self._video_library.get_video(video_id) is None:
            print("Cannot remove video from", playlist_name+": Video does not exist")
            return

        for n in range(1, len(self.playlists[playlist_pos])):
            if self.playlists[playlist_pos][n] == video_id:
                del(self.playlists[playlist_pos][n])
                print("Removed video from", playlist_name+":", self._video_library.get_video(video_id).title)
                return

        print("Cannot remove video from", playlist_name+": Video is not in playlist")





    def clear_playlist(self, playlist_name):
        nameExist = False
        playlist_pos = -1
        for i in range(0, len(self.playlists)):
            if self.playlists[i][0].lower() == playlist_name.lower():
                playlist_pos = i
                nameExist = True

        if not nameExist:
            print("Cannot remove video from", playlist_name+": Playlist does not exist")
        else:

            for n in range(len(self.playlists[playlist_pos])-1, 0, -1):
                del(self.playlists[playlist_pos][n])
            print("Successfully removed all videos from", playlist_name)

    def delete_playlist(self, playlist_name):
        nameExist = False
        playlist_pos = -1
        for i in range(0, len(self.playlists)):
            if self.playlists[i][0].lower() == playlist_name.lower():
                playlist_pos = i
                nameExist = True

        if not nameExist:
            print("Cannot delete playlist", playlist_name + ": Playlist does not exist")
        else:
            del(self.playlists[playlist_pos])
            print("Deleted playlist:", playlist_name)

    def search_videos(self, search_term):
        videos_info = self._video_library.get_all_videos()
        videos_found = []
        for i in range(0, len(self._video_library.get_all_videos())):
            if search_term.lower() in videos_info[i].title.lower():
                videos_found.append(videos_info[i])

        if len(videos_found)==0:
            print("No search results for", search_term)
        else:
            print("Here are the results for",search_term+":")
            for n in range(0, len(videos_found)):
                display_number = n+1
                print(display_number,":", videos_found[n].title,videos_found[n].video_id,videos_found[n].tags)

            choice = input("Would you like to play any of the above? If yes, specify the number of the video.If your answer is not a valid number, we will assume it's a no.")
            try:
                for x in range(0, len(videos_found)):
                    if int(choice) == x+1:
                        self.play_video(videos_found[x].video_id)
            except:return



    def search_videos_tag(self, video_tag):
        videos_info = self._video_library.get_all_videos()
        videos_found = []
        for i in range(0, len(self._video_library.get_all_videos())):
            for z in range(0,len(videos_info[i].tags)):
                if video_tag.lower() == videos_info[i].tags[z].lower():
                    videos_found.append(videos_info[i])

        if len(videos_found)==0:
            print("No search results for", video_tag)
        else:
            print("Here are the results for",video_tag+":")
            for n in range(0, len(videos_found)):
                display_number = n+1
                print(display_number,":", videos_found[n].title,videos_found[n].video_id,videos_found[n].tags)

            choice = input("Would you like to play any of the above? If yes, specify the number of the video.If your answer is not a valid number, we will assume it's a no.")
            try:
                for x in range(0, len(videos_found)):
                    if int(choice) == x+1:
                        self.play_video(videos_found[x].video_id)
            except:return

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
