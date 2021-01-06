from chat import mybot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# trainer = ChatterBotCorpusTrainer(mybot)


# trainer = ChatterBotCorpusTrainer(mybot)

# trainer.train(
#     "datasets"
# )


# Get a response for some unexpected input
while True:
    try:
        user_input = input()

        bot_response = mybot.get_response(user_input)

        print(bot_response)
    
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

    