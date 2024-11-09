from azure.storage.queue import QueueClient

# Your storage account's connection string
connection_string = "DefaultEndpointsProtocol=https;AccountName=cloudrisedevaccount;AccountKey=7ipIxl1h4LgKm8j1ZqpJ3keWmUmFVOMSf70f6UtP0coujQ0VHkFdZou+nJeuFZVpA5INHBS1Zc2L+AStpFxQCA==;EndpointSuffix=core.windows.net"

# The name of your Azure Queue
queue_name = "cloudrisedev-messages-queue"

# Create the QueueClient object directly using the connection string and queue name
queue_client = QueueClient.from_connection_string(connection_string, queue_name)

# Receive messages from the queue
messages = queue_client.receive_messages()

for message in messages:
    print("Message received:", message.content)
    # Optionally process the message here...

    # When you're done processing the message, delete it
    queue_client.delete_message(message)
    print("Message deleted from the queue:", message.id)
