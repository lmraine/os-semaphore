import pytest
from buffer_sem import Buffer, Producer, Consumer

@pytest.fixture
def buffer():
    return Buffer(5)

def test_initial_state(buffer):
    assert buffer.size == 5
    assert len(buffer.buffer) == 5
    assert buffer.in_pointer == 0
    assert buffer.out_pointer == 0

def test_produce_consume(buffer):
    producer = Producer(buffer, 1)
    consumer = Consumer(buffer, 1)

    producer.produce(10)
    assert buffer.buffer[0] == 10
    assert buffer.in_pointer == 1

    item = consumer.consume()
    assert item == 10
    assert buffer.out_pointer == 1

#TODO: TEST IF COSUMER IF BUFFER IS FULL
#TODO: TEST IF PRODUCER IF BUFFER IS EMPTY
def test_buffer_full(buffer):
    producer = Producer(buffer, 1)
    for i in range(buffer.size):
        producer.produce(i)
    assert buffer.in_pointer == 0
    assert buffer.buffer == [0, 1, 2, 3, 4]

def test_buffer_empty(buffer):
    consumer = Consumer(buffer, 1)
    with pytest.raises(Exception):
        consumer.consume()

def test_producer_produce(buffer):
    producer = Producer(buffer, 1)
    producer.produce(10)
    assert buffer.buffer[0] == 10
    assert buffer.in_pointer == 1

def test_producer_produce_full_buffer(buffer):
    producer = Producer(buffer, 1)
    for i in range(buffer.size):
        producer.produce(i)
    with pytest.raises(Exception):
        producer.produce(10)

def test_consumer_consume(buffer):
    producer = Producer(buffer, 1)
    consumer = Consumer(buffer, 1)
    producer.produce(10)
    item = consumer.consume()
    assert item == 10
    assert buffer.out_pointer == 1

if __name__ == "__main__":
    pytest.main()