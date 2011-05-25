import sys
import ReplicantSrvrImpl as impl
import protobuf.socketrpc.server as server
import chunks_pb2

if not len(sys.argv) > 1:
    print 'Parameter missing!'
    sys.exit()

if sys.argv[1] == 'server':
    replicant_service = impl.ReplicantSrvrImpl()
    server = server.SocketRpcServer(8090)
    server.registerService(replicant_service)
    
    # Start the server
    print 'Serving on port 8090'
    server.run()
if sys.argv[1] == 'client':
    from protobuf.socketrpc import RpcService
    import logging

    log = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)
    
    # Server details
    hostname = 'localhost'
    port = 8090
    
    
    # Create a request
    request = chunks_pb2.Chunk()
    request.id = 'Id del chunk'
    request.owner = 'Owner del chunk'
    request.chunk = 'El contenido del chunk'
    
    # Create a new service instance
    service = RpcService(chunks_pb2.ReplicantSrvr_Stub,
                         port,
                         hostname)
    
    
    def callback(request, response):
        """Define a simple async callback."""
        log.info('Asynchronous response :' + response.__str__())
    
    # Make an asynchronous call
    try:
        log.info('Making asynchronous call')
        response = service.SendChunk(request, callback=callback)
    except Exception, ex:
        log.exception(ex)
    
    # Make a synchronous call
    try:
        log.info('Making synchronous call')
        response = service.SendChunk(request, timeout=10000)
        log.info('Synchronous response: ' + response.__str__())
    except Exception, ex:
        log.exception(ex)
