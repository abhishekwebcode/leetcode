class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], me: int, level: int) -> List[str]:
        wvm={}
        for i,v in enumerate(watchedVideos):
            wvm[i]=set(watchedVideos[i])
        fm={}
        for i,v in enumerate(friends):
            fm[i]=set(friends[i])
        visited=set([me])
        q=[me]
        for _ in range(level):
            # add q's friends in q
            temp=set()
            for person in q:
                for friend in friends[person]:
                    if friend!=me and friend not in visited:
                        temp.add(friend)
                        visited.add(friend)
            q=temp
        print((q))
        cnt=Counter()
        for person in q:
            for video in wvm[person]:
                cnt[video]+=1
        return sorted(cnt.keys(),key=lambda x:(cnt[x],x))