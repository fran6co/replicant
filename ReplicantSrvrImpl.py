import chunks_pb2

class ReplicantSrvrImpl(chunks_pb2.ReplicantSrvr):
    def SendChunk(self, controller, request, done):
        print "Send Chunk!"

        # Print the request
        print request

        id = request.id
        owner = request.owner

        # Create a reply
        response = chunks_pb2.ChunkInfo()
        
        response.id = id
        response.owner = owner
        response.frozen = 1

        # We're done, call the run method of the done callback
        done.run(response)

    def GetChunk(self, controller, request, done):
        print "Get Chunk!"
        # Print the request
        print request

        id = request.id
        owner = request.owner

        # Create a reply
        response = chunks_pb2.Chunk()
        
        response.id = id
        response.owner = owner
        response.chunk = 'test!'

        # We're done, call the run method of the done callback
        done.run(response)
    
    def UnfreezeChunk(self, controller, request, done):
        print "Get Chunk!"
        # Print the request
        print request

        id = request.id
        owner = request.owner

        # Create a reply
        response = chunks_pb2.ChunkInfo()
        
        response.id = id
        response.owner = owner
        response.frozen = 0

        # We're done, call the run method of the done callback
        done.run(response)
        