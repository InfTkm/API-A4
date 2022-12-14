
from concurrent import futures
import logging

import grpc
import inventory_pb2
import inventory_pb2_grpc


class Inventory(inventory_pb2_grpc.InventoryServiceServicer):
    books = []
    def CreateBook(self, req, context):
        book = {
            "ISBN": req.ISBN,
            "title": req.title,
            "author":req.author,
            "genre": list(req.genre),
            "year": req.year
        }
        self.books.append(book)
        return inventory_pb2.Book(ISBN=book['ISBN'], title=book['title'], author=book['author'], genre=book['genre'], year=book['year'])

    def GetBook(self, req, context):
        isbn = req.ISBN
        for book in self.books:
            if book['ISBN'] == isbn:
                return inventory_pb2.Book(ISBN=book['ISBN'], title=book['title'], author=book['author'], genre=book['genre'], year=book['year'])
        return inventory_pb2.Book(ISBN="-1", title="", author="", genre=[], year=-1)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_InventoryServiceServicer_to_server(Inventory(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()