from inventory_client import InventoryClient
def getBookTitles(client, ISBNs):
    titles = []
    for ISBN in ISBNs:
        book = client.get_book(ISBN)
        titles.append(book.title)
    return titles

if __name__ == "__main__":
    client = InventoryClient("[::]:50051")
    titles = getBookTitles(client, ["0", "1", "3"])
    print(titles)
