import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--message", "-m", help="Le message a envoyer")
parser.add_argument("-read", action="store_true")
args = parser.parse_args()

print(args.message)
print(args.read)

if args.read:
    import simple_queue_read
else:
    message = args.message
    import simple_queue_publish as pub
    pub.sendMessage(message)