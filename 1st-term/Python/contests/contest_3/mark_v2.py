import codecs
import struct


def get_messages_from_server(score_dump):
    messages_from_server = []
    while True:
        length = struct.unpack('>H', score_dump[4:6])[0]
        # print(length)
        message = score_dump[48:40 + length]
        messages_from_server.append(codecs
                                    .decode(message, 'hex')
                                    .decode('utf-8'))
        score_dump = score_dump[40 + length:]
        if len(score_dump) == 0:
            break
    return messages_from_server


if __name__ == '__main__':
    # score_dump = open('score_dump.bin', 'rb').read()
    # messages = get_messages_from_server(score_dump)
    print(59)
