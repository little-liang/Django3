import queue

class Chat(object):
    def __init__(self):
        self.msg_queue = queue.Queue()


    def get_msg(self, request):
        new_msgs = []
        if self.msg_queue.qsize() > 0:
            for msg in range(self.msg_queue.qsize()):
                new_msgs.append(self.msg_queue.get_nowait())
        else:  #no new msg ,wait 60s
            try:
                print("-------------no new msg, going to wait 60s------------")
                new_msgs.append(self.msg_queue.get(timeout=60))
                print("new msg [%s]" % (new_msgs))
            except queue.Empty:
                print("time out no new msg for user [%s]" % (request.user.userprofile.name))
        print("found new msg [%s]" % (len(new_msgs)))
        return new_msgs

