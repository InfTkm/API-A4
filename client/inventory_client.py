import grpc
import inventory_pb2
import inventory_pb2_grpc

class InventoryClient():
    def __init__(self, url):
        self.stub = inventory_pb2_grpc.InventoryServiceStub(grpc.insecure_channel(url))

    def get_book(self, ISBN):
        return self.stub.GetBook(inventory_pb2.GetBookRequest(ISBN=ISBN))

    def create_book(self, book):
        if "genre" not in book:
            book["genre"] = []
        return self.stub.CreateBook(inventory_pb2.Book(
            ISBN=book['ISBN'],
            title=book['title'],
            author=book['author'],
            genre=book['genre'],
            year=book['year']
        ))
